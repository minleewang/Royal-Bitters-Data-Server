from abc import ABC, abstractmethod


class AlcoholDescriptionRepository(ABC):

    @abstractmethod
    def create(self, alcohol, description):
        pass

    @abstractmethod
    def findByAlcohol(self, alcohol):
        pass

