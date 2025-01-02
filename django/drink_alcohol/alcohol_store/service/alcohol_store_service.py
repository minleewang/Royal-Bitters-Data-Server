from abc import ABC, abstractmethod


class AlcoholStoreService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):  # 전체 리스트 반환, (1페이지에 10개만 이런식)
        pass

    @abstractmethod
    def createAlcoholInfo(self, title, price, description, image, alcoholCategory):
        pass   # 홈페이지에 올릴 주류 정보를 등록

    @abstractmethod
    def readAlcoholInfo(self, id): # id를 가지고 술 정보를 불러오기
        pass