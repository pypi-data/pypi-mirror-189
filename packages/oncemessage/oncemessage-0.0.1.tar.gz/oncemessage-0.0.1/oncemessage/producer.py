#!/usr/bin/env python3

import json
import re
import time
from datetime import datetime
from typing import Union

import codefast as cf

from .db import get_redis


class TimeRecognizer(object):

    def seconds_diff(self, text: str) -> int:
        # parse datetime from text and return seconds difference
        parsed = self.parse(text)
        if parsed is None:
            # maybe pure seconds is given
            if text.isdigit():
                return int(text)
            else:
                cf.warning('Cannot parse time from "{}"'.format(text))
                return 0
        else:
            seconds = int((parsed - datetime.now()).total_seconds())
            if seconds < 0:
                cf.warning('Time in past: {}'.format(text))
            return max(seconds, 0)

    def parse(self, text: str) -> Union[datetime, None]:
        r = re.search(
            r'(((?P<month>[\w+|\d+])?([\/\:\-]))?(?P<day>\d+)([\s]+))?(?P<hour>\d+)[\:\-\/](?P<minute>\d+)([\:\-\/](?P<second>\d+))?$',
            text)
        if r:
            year = datetime.now().year
            month = int(r.group('month') or datetime.now().month)
            day = int(r.group('day') or datetime.now().day)
            hour = int(r.group('hour'))
            minute = int(r.group('minute'))
            second = int(r.group('second') or 0)
            date_str = '{}-{}-{} {}:{}:{}'.format(year, month, day, hour,
                                                  minute, second)
            cf.info('parsed date: {}'.format(date_str))
            return datetime(year, month, day, hour, minute, second)
        return None


def create_message(date_like: str, content: str, redis_url:str) -> bool:
    # Parse expire time from `date_like` string and create a message
    expire_time = TimeRecognizer().seconds_diff(str(date_like))
    msg = {'timestamp': time.time() + expire_time, 'content': content}
    key = 'oncemessage:{}'.format(cf.md5sum(str(msg)))
    cf.info('posting oncemssage {}'.format(msg))
    resp = get_redis(redis_url).set(key,
                           json.dumps(msg),
                           ex=max(expire_time * 2, 86400))
    cf.info(resp)
    return resp
