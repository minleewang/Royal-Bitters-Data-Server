from beer.entity.beer_price import BeerPrice
from beer.repository.beer_price_repository import BeerPriceRepository


class BeerPriceRepositoryImpl(BeerPriceRepository):
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

    # Beer_price 테이블에서 create
    # 이 테이블에는 id(PK), Beer(FK), price 이렇게 셋이 있음
    # 이 두개(Beer(FK), price )를 create
    def create(self, beer, price):
        return BeerPrice.objects.create(beer=beer, price=price)


    def findByBeer(self, beer):
        return BeerPrice.objects.get(beer=beer)




