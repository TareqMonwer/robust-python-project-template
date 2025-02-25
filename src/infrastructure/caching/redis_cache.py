import redis


class RedisCache:
    def __init__(self, redis_url="redis://localhost"):
        self.client = redis.from_url(redis_url)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, ttl=3600):
        self.client.set(key, value, ex=ttl)
