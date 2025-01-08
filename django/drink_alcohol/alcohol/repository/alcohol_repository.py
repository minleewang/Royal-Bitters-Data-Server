from abc import ABC, abstractmethod


class AlcoholRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):
        pass

    @abstractmethod
    def create(self, title, price, type, image):
        pass

    # alcohol, alcohol_image 의 DB에는 각 id가 PK로 각각 있음
    @abstractmethod
    def findById(self, id):
        pass

    #@abstractmethod
    #def findAll(self):
    #    pass