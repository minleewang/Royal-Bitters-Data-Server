from abc import ABC, abstractmethod


class WineRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):  # 전체 리스트 반환, (1페이지에 10개만 이런식)
        pass

    @abstractmethod
    def create(self, wine):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def letRoleTypeWine(self):
        pass