from abc import ABC, abstractmethod


class WhiskeyPriceRepository(ABC):

    @abstractmethod
    def create(self, whiskey, price):
        pass

    @abstractmethod
    def findByWhiskey(self, whiskey):
        pass