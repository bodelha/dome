import os
import json
from pymemcache.client import base


class Cache:
    def __init__(self, host=None, port=11211):
        self.client = base.Client((os.getenv("MEMCACHED_HOST", host), port))

    def set(self, key, value, expire=60):
        """Salva um valor no cache, atualizando o TTL se a chave já existir."""
        json_value = json.dumps(value)

        if self.client.get(key):
            self.client.set(key, json_value, expire)
        else:
            self.client.set(key, json_value, expire)

    def get(self, key):
        """Recupera um valor do cache, desserializando-o de JSON."""
        result = self.client.get(key)
        if result:
            return json.loads(result)
        return None

    def delete(self, key):
        """Exclui um item do cache pelo seu nome de chave."""
        self.client.delete(key)
