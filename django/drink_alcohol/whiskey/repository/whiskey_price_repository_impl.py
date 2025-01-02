from whiskey.entity.whiskey_price import WhiskeyPrice
from whiskey.repository.whiskey_price_repository import WhiskeyPriceRepository


class WhiskeyPriceRepositoryImpl(WhiskeyPriceRepository):
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

    # Whiskey_price 테이블에서 create
    # 이 테이블에는 id(PK), Whiskey(FK), price 이렇게 셋이 있음
    # 이 두개(Whiskey(FK), price )를 create
    def create(self, whiskey, price):
        return WhiskeyPrice.objects.create(whiskey=whiskey, price=price)


    def findByWhiskey(self, whiskey):
        return WhiskeyPrice.objects.get(whiskey=whiskey)




