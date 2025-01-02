from abc import ABC, abstractmethod


class WhiskeyImageRepository(ABC):

    @abstractmethod
    def create(self, whiskey, image):
        pass

    @abstractmethod
    def findByWhiskey(self, whiskey):
        pass