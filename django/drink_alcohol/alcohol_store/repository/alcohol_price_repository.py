from abc import ABC, abstractmethod


class AlcoholPriceRepository(ABC):

    @abstractmethod
    def create(self, alcohol, price):
        pass

    @abstractmethod
    def findByAlcohol(self, alcohol):
        pass