from abc import ABC, abstractmethod


class WhiskeyDescriptionRepository(ABC):

    @abstractmethod
    def create(self, whiskey, description):
        pass

    @abstractmethod
    def findByWhiskey(self, whiskey):
        pass