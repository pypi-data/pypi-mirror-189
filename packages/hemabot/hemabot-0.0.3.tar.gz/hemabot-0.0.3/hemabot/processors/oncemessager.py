#!/usr/bin/env python
import codefast as cf


class OnceMessager(object):

    def match(self, text: str) -> bool:
        return 'oncemessage' in text

    def process(self, text: str, updater: "Updater") -> None:
        _, date_like, content = text.split(' ', 2)
        url = 'https://uuid.fly.dev/newmessage'
        resp = cf.net.post(url,
                           json={
                               'content': content,
                               'date_like': date_like
                           })
        cf.info(resp.json())
        updater.message.reply_text(str(resp.json()))
