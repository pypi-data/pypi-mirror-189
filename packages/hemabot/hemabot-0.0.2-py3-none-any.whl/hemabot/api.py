#!/usr/bin/env python
import re
from concurrent.futures import ThreadPoolExecutor
from typing import List
from uuid import uuid4

import codefast as cf
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from hemabot.auth import auth

from .processors.deepl import DeeplAPI, DeeplProcessor
from .processors.oncemessager import OnceMessager
from .processors.twitter import TwitterVideoDownloader


class TextClient:

    @staticmethod
    def run_in_order(objects: List, text: str, update: Update) -> bool:
        obj = next((o for o in objects if o.match(text)), None)
        if obj:
            cf.info("Matched {}".format(obj.__class__.__name__))
            obj.process(text, update)


def get_text_handler(text: str) -> MessageHandler:
    reflection = {
        'oncemessage': OnceMessager,
        'deepl': DeeplProcessor,
        'twitter': TwitterVideoDownloader
    }
    try:
        if re.findall(r'[\u4e00-\u9fff]+', text):  # contain chinese
            label = 'deepl'
        else:
            params = {'text': text}
            resp = cf.net.post('https://cf.ddot.cc/bothelper/', json=params)
            js = resp.json()
            cf.info('bothelper resp: {}'.format(js))
            label = js['label']
    except Exception as e:
        cf.info(e)
        label = ''

    return reflection.get(label, None)


class Psycho(object):

    def __init__(self):
        cf.info('start Psycho TG bot.')
        self.deeplapi = DeeplAPI()
        self.bot_name = 'hemahema'
        self.text = ''
        self.pool = ThreadPoolExecutor(23)

    def deepl(self, update: Update, context: CallbackContext) -> None:
        '''deepl trans'''
        text = ' '.join(context.args)
        result = self.deeplapi.translate(text)['translations'].pop()['text']
        update.message.reply_text(result)

    def text_handler(self, update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        if not update.message:
            # Avoid error when user sends a message without text
            return
        text = update.message.text
        self.text = text
        cf.io.write(text, '/tmp/wechat.txt')
        cf.info(f"received text: {text}")
        processor = get_text_handler(text)
        if processor:
            update.message.reply_text('Match {}'.format(processor.__name__))
            self.pool.submit(processor().process, text, update)
        else:
            update.message.reply_text('Input {} found No match'.format(text))

    def file_handler(self, update: Update, context: CallbackContext) -> None:
        ''' save phone to cloud
        # https://stackoverflow.com/questions/50388435/how-save-photo-in-telegram-python-bot
        '''
        _files = []
        if update.message.document:
            # uncompressed photo
            file_id = update.message.document.file_id
            file_type = update.message.document.mime_type.split('/')[-1]

        elif update.message.photo:
            # compressed photo
            file_type = 'jpeg'
            photoes = update.message.photo
            cf.info('receive photos', photoes)
            for p in photoes[-1:]:
                file_id = p.file_id
                file_name = f'{uuid4()}.{file_type}'
                obj = context.bot.get_file(file_id)
                obj.download(file_name)
                _files.append(file_name)
                cf.info(f"received photo: {file_name}")

        elif update.message.video:
            file_type = 'mp4'
            video = update.message.video
            cf.info('receive videos', video)
            file_id = video['file_id']
            file_name = f'{uuid4()}.{file_type}'
            obj = context.bot.get_file(file_id)
            obj.download(file_name)
            _files.append(file_name)
            cf.info(f"received video: {file_name}")

        else:
            update.message.reply_text(
                'No photo nor ducument detected from {}'.format(
                    str(update.message)))
            return


def start_bot() -> None:
    """Run bot
    update.message methods: https://docs.pyrogram.org/api/bound-methods/Message.reply_text
    """
    psy = Psycho()
    updater = Updater(auth.hema_bot)
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler(("deepl", 'dpl'), psy.deepl))
    dispatcher.add_handler(MessageHandler(Filters.text, psy.text_handler))
    dispatcher.add_handler(
        MessageHandler(Filters.document | Filters.photo | Filters.video,
                       psy.file_handler))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start_bot()
