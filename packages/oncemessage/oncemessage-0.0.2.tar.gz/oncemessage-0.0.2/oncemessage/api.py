#!/usr/bin/env python

import json
import time
from typing import Dict, List
from urllib.parse import quote_plus

import codefast as cf
import requests
from codefast.patterns.pipeline import Component, Pipeline

from .db import get_redis


class ctx(object):
    bark_host = None
    redis_client = None


class GetAllMessages(Component):

    def process(self) -> List[Dict]:
        key_prefix = 'oncemessage:'
        resp = []
        for key in ctx.redis_client.keys(key_prefix + '*'):
            content = ctx.redis_client.get(key).decode()
            resp.append(json.loads(content))
        return resp


class FilterOnTimeMessage(Component):
    """Filter out messages that are not on time
    """

    def process(self, messages: List[Dict]) -> List[Dict]:
        return [msg for msg in messages if msg['timestamp'] < time.time()]


class PostMessage(Component):

    def post(self, content: str) -> bool:
        try:
            cf.info('posting message {}'.format(content))
            url = ctx.bark_host + quote_plus(content)
            url += '?icon=https://file.ddot.cc/tmp/logo_apple.png'
            resp = requests.get(url)
            return resp.status_code == 200
        except Exception as e:
            cf.error(e)
            return False

    def process(self, messages) -> List[Dict]:
        return [msg for msg in messages if self.post(msg['content'])]


class DeletePostedMessage(Component):

    def process(self, messages) -> List[Dict]:
        for msg in messages:
            md5 = cf.md5sum(str(msg))
            ctx.redis_client.expire('oncemessage:' + md5, 0)
        return []


def run_once(bark_host: str, redis_url: str):
    ctx.bark_host = bark_host
    if ctx.redis_client is None:
        ctx.redis_client = get_redis(redis_url)
    
    Pipeline([
        GetAllMessages(),
        FilterOnTimeMessage(),
        PostMessage(),
        DeletePostedMessage()
    ]).process()
