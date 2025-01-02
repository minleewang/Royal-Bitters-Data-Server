from abc import ABC, abstractmethod


class WinePriceRepository(ABC):

    @abstractmethod
    def create(self, wine, price):
        pass

    @abstractmethod
    def findByWine(self, wine):
        pass