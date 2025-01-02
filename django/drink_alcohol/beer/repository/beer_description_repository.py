from abc import ABC, abstractmethod


class BeerDescriptionRepository(ABC):

    @abstractmethod
    def create(self, beer, description):
        pass

    @abstractmethod
    def findByBeer(self, beer):
        pass
