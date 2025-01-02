from abc import ABC, abstractmethod


class AlcoholCategoryRepository(ABC):

    @abstractmethod
    def create(self, alcohol, alcoholCategory):
        pass

    @abstractmethod
    def findByAlcohol(self, alcohol):
        pass
