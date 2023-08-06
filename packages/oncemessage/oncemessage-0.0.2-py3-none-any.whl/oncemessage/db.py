#!/usr/bin/env python3
import redis


def get_redis(url: str):
    return redis.Redis.from_url(url)
