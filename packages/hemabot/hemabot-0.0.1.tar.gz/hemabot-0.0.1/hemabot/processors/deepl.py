#!/usr/bin/env python3
import json
import time

import codefast as cf
from rich import print
from typing import List, Union, Callable, Set, Dict, Tuple, Optional, Any
from hemabot.auth import auth 

class DeeplAPI(object):
    '''Deepl tranlation API'''

    def __init__(self) -> None:
        self._url = 'https://api-free.deepl.com/v2'
        self._headers = '''Host: api-free.deepl.com
            User-Agent: YourApp
            Accept: */*
            Content-Length: [length]
            Content-Type: application/x-www-form-urlencoded'''
        self._token = auth.deepl_token
        self._params = {'auth_key': self._token}

    def do_request(self, api_path: str) -> dict:
        resp = cf.net.post(self._url + api_path,
                           headers=cf.net.parse_headers(self._headers),
                           data=self._params)
        if resp.status_code != 200:
            raise Exception(resp)
        cf.io.say(resp.json())
        return resp.json()

    @property
    def stats(self):
        return self.do_request('/usage')

    def translate(self, text: str) -> str:
        target_lang = 'EN' if cf.nstr(text).is_cn() else 'ZH'
        self._params['text'] = text
        self._params['target_lang'] = target_lang
        return self.do_request('/translate')

    def document(self, file_name: str) -> dict:
        text = cf.io.reads(file_name)
        target_lang = 'EN' if cf.nstr(text).is_cn() else 'ZH'
        _auth = self._token
        cmd = f'curl https://api-free.deepl.com/v2/document \
                -F "file=@{file_name}" \
                -F "auth_key={_auth}" \
                -F "target_lang={target_lang}"'

        resp = json.loads(cf.shell(cmd))
        cf.info(resp)
        _id, _key = resp['document_id'], resp['document_key']
        while True:
            resp = self.get_document_status(_id, _key)
            if resp['status'] == 'done':
                break
            time.sleep(3)

        _doc = self.get_translated_document(_id, _key)
        print(_doc)
        return _doc

    def get_document_status(self, doc_id: str, doc_key: str) -> dict:
        cf.info(f'Getting document status {doc_id} {doc_key}')
        self._params['document_key'] = doc_key
        return self.do_request(f'/document/{doc_id}')

    def get_translated_document(self, doc_id: str, doc_key: str) -> dict:
        cmd = f'curl https://api-free.deepl.com/v2/document/{doc_id}/result \
                -d auth_key={self._token} \
                -d document_key={doc_key}'

        return cf.shell(cmd)


class DeeplProcessor(object):
    """Translate with Deepl
    """
    def __init__(self) -> None:
        self.deeplapi = DeeplAPI()

    def match(self, _text: str) -> bool:
        if _text.startswith('http'):
            return False
        return True

    def run(self, text: str, update: 'Update') -> str:
        update.message.reply_text(
            self.deeplapi.translate(text)['translations'].pop()['text'])
        return True

    def process(self, text: str, update: 'Update') -> str:
        if self.match(text):
            return self.run(text, update)
