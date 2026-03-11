
class ConfigManager:
    def __init__(self, path: str):
        self.path = path
        self._cache = {}

    def get(self, key):
        return self._cache.get(key)

