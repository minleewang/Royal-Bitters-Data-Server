from wine.entity.wine_price import WinePrice
from wine.repository.wine_price_repository import WinePriceRepository


class WinePriceRepositoryImpl(WinePriceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # Wine_price 테이블에서 create
    # 이 테이블에는 id(PK), Wine(FK), price 이렇게 셋이 있음
    # 이 두개(Wine(FK), price )를 create
    def create(self, wine, price):
        return WinePrice.objects.create(wine=wine, price=price)


    def findByWine(self, wine):
        return WinePrice.objects.get(wine=wine)




