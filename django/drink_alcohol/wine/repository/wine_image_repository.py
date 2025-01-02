from abc import ABC, abstractmethod


class WineImageRepository(ABC):

    @abstractmethod
    def create(self, wine, image):
        pass

    @abstractmethod
    def findByWine(self, wine):
        pass