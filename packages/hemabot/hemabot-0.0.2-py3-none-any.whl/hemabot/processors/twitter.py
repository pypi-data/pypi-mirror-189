import hashlib
import json
from abc import ABCMeta, abstractmethod
from typing import Union

import codefast as cf
from telegram import Update


class TextProcessor(metaclass=ABCMeta):
    '''Base class for processing text passed from user'''

    def match(self, text: str) -> bool:
        pass

    def process(self, text: str, update: Update) -> str:
        if self.match(text):
            return self.run(text, update)

    @abstractmethod
    def run(self, text: str, update: Update) -> bool:
        return False


class OldFilesCleaner(object):

    def labor(self):
        # clean files in /tmp older than 7 day
        cf.shell('find /tmp -type f -mtime +7 -exec rm -f {} \;')



class VideoCache(object):

    def __init__(self) -> None:
        self.redis = cf.mydb('/tmp/videocache.db')

    def query_video_id(self, digest_value: str) -> Union[str, None]:
        if self.redis.exists(digest_value):
            return self.redis.get(digest_value)
        return None

    def save_video_id(self, digest_value: str, message: dict) -> None:
        self.redis.set(digest_value, message['video']['file_id'])


class TwitterVideoDownloader(TextProcessor):

    def match(self, text: str) -> bool:
        return text.startswith('https://twitter.com/')

    def run(self, text: str, update: Update) -> bool:
        update.message.delete()
        message = update.message.reply_text(f'Downloading video from {text}')
        filename = hashlib.md5(text.encode('utf-8')).hexdigest()
        video = f"/tmp/{filename}.mp4"
        cacher = VideoCache()
        
        try:
            video_id = cacher.query_video_id(filename)
            if video_id is not None:
                message.edit_text(f'Video already cached.')
                cf.info('file id is {}'.format(video_id))
                update.message.reply_video(video_id, supports_streaming=True)
            else:
                for _ in range(10):
                    if not cf.io.exists(video):
                        cf.shell('youtube-dl -f best "{}" -o "{}"'.format(
                            text, video))
                cf.info(f'video {video} downloaded.')
                message.edit_text(f'Uploading video ...')
                _msg = update.message.reply_video(open(video, 'rb'),
                                                  supports_streaming=True)
                js = json.loads(_msg.to_json())
                cacher.save_video_id(filename, js)
            message.delete()
            cf.info(f'video {video} sent.')
        except Exception as e:
            update.message.reply_text(str(e))

        OldFilesCleaner().labor()
        return True
