from abc import ABC, abstractmethod


class RedisCacheService(ABC):
    @abstractmethod
    def storeKeyValue(self, key, value):
        pass  # Key Value 저장

    @abstractmethod
    def getValueByKey(self, key):
        pass  # Get Value By Key

    @abstractmethod
    def deleteKey(self, key):
        pass  # Key 제거