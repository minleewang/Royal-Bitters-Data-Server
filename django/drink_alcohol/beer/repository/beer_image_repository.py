from abc import ABC, abstractmethod


class BeerImageRepository(ABC):

    @abstractmethod
    def create(self, beer, image):
        pass

    @abstractmethod
    def findByBeer(self, beer):
        pass