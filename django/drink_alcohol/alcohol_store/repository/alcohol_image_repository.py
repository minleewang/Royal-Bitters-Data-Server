from abc import ABC, abstractmethod


class AlcoholImageRepository(ABC):

    @abstractmethod
    def create(self, alcohol, image):
        pass

    @abstractmethod
    def findByAlcohol(self, alcohol):
        pass