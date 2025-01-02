from abc import ABC, abstractmethod


class WineDescriptionRepository(ABC):

    @abstractmethod
    def create(self, wine, description):
        pass

    @abstractmethod
    def findByWine(self, wine):
        pass
