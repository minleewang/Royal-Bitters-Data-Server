from abc import ABC, abstractmethod


class AlcoholService(ABC):

    @abstractmethod
    def requestAlcoholList(self, page, perPage):
        pass   # 모든 주류 데이터 반환

    @abstractmethod
    def createAlcoholList(self, title, price, image, type):
        pass

    @abstractmethod
    def readAlcoholById(self, id):
        pass

    #@abstractmethod
    #def readAlcoholByType(self, type):
    #    pass

    # GPT 가 제안한 service에 들어갈 내용
    # get_all_alcohols(): 모든 주류 데이터 반환
    # get_alcohol_by_id(id: int): 특정 주류 데이터 반환
    # get_alcohols_by_type(type: str): 특정 타입(BEER, WHISKEY, WINE)의 주류 반환