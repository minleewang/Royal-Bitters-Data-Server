from abc import ABC, abstractmethod


class AlcoholRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):  # 전체 리스트 반환, (1페이지에 10개만 이런식)
        pass

#    @abstractmethod
#    def findAll(self):
#        pass

    @abstractmethod
    def create(self, title): # 뭘 create 하는데
        pass

#    @abstractmethod
#    def findById(self, id):
#        pass