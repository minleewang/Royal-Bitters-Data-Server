from django.db import transaction

from alcohol.entity.role_type import RoleType
from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from alcohol.service.alcohol_service import AlcoholService
from beer.repository.beer_image_repository_impl import BeerImageRepositoryImpl
from beer.repository.beer_price_repository_impl import BeerPriceRepositoryImpl
from beer.repository.beer_repository import BeerRepository
from beer.repository.beer_repository_impl import BeerRepositoryImpl
from whiskey.repository.whiskey_image_repository_impl import WhiskeyImageRepositoryImpl
from whiskey.repository.whiskey_price_repository_impl import WhiskeyPriceRepositoryImpl
from whiskey.repository.whiskey_repository_impl import WhiskeyRepositoryImpl
from wine.repository.wine_image_repository_impl import WineImageRepositoryImpl
from wine.repository.wine_price_repository_impl import WinePriceRepositoryImpl
from wine.repository.wine_repository_impl import WineRepositoryImpl


# 기본적으로 Alcohol 데이터를 생성, 읽기, 수정, 삭제하는 기능이 필요
# 수정, 삭제는 안하기로 Create,Read 이 두개만 합시다.

class AlcoholServiceImpl(AlcoholService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()

            # beer
            cls.__instance.__beerRepository = BeerRepositoryImpl.getInstance()
            cls.__instance.__beerPriceRepository = BeerPriceRepositoryImpl.getInstance()
            cls.__instance.__beerImageRepository = BeerImageRepositoryImpl.getInstance()
            # alcohol에서 type 가져와야함

            # whiskey
            cls.__instance.__whiskeyRepository = WhiskeyRepositoryImpl.getInstance()
            cls.__instance.__whiskeyPriceRepository = WhiskeyPriceRepositoryImpl.getInstance()
            cls.__instance.__whiskeyImageRepository = WhiskeyImageRepositoryImpl.getInstance()
            # alcohol에서 type 가져와야함

            # wine
            cls.__instance.__wineRepository = WineRepositoryImpl.getInstance()
            cls.__instance.__winePriceRepository = WinePriceRepositoryImpl.getInstance()
            cls.__instance.__wineImageRepository = WineImageRepositoryImpl.getInstance()
            # alcohol에서 type 가져와야함

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def requestAlcoholList(self, page, perPage):
        return self.__alcoholRepository.list(page, perPage)


    def createAlcohol(self, title, price, type, image):

        #alcohol_type = Alcohol.objects.first()
        #findByType??
        #findBy???

        if alcohol["type"] == RoleType.BEER.value:
            with transaction.atomic():
                savedBeer = self.__beerRepository.create(title)
                self.__beerPriceRepository.create(savedBeer, price)
                self.__beerImageRepository.create(savedBeer, image)
                #self.__beerType = RoleType.BEER.value beerTypeRepository 없는데..


        # if 데이터가 Whiskey라면
        with transaction.atomic():
            savedWhiskey = self.__whiskeyRepository.create(title)
            self.__whiskeyPriceRepository.create(savedWhiskey, price)
            self.__whiskeyImageRepository.create(savedWhiskey, image)
            # self.__beerType 타입은 어쩌지

        # if 데이터가 Wine이라면
        with transaction.atomic():
            savedWine = self.__wineRepository.create(title)
            self.__winePriceRepository.create(savedWine, price)
            self.__wineImageRepository.create(savedWine, image)
            # self.__beerType 타입은 어쩌지

            
    def readAlcohol(self, id):

        foundAlcohol = self.__alcoholRepository.findById(id)
        print(f"foundAlcohol: {foundAlcohol}")

        readAlcoholInfo = {
            'id': foundAlcohol.getAlcoholId(),
            'title': foundAlcohol.getAlcoholTitle(),
            'price': foundAlcohol.getAlcoholPrice(),
            'image': foundAlcohol.getAlcoholImage(),
            'type': foundAlcohol.getAlcoholType()
            }

        return readAlcoholInfo