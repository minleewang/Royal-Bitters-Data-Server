from abc import ABC, abstractmethod


class AlcoholService(ABC):

    @abstractmethod
    def requestAlcoholList(self, page, perPage):
        pass

    @abstractmethod
    def createAlcohol(self, title, price, image, type):
        pass

    @abstractmethod
    def readAlcohol(self, id):
        pass