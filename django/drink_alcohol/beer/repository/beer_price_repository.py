from abc import ABC, abstractmethod


class BeerPriceRepository(ABC):

    @abstractmethod
    def create(self, beeer, price):
        pass

    @abstractmethod
    def findByBeer(self, beer):
        pass