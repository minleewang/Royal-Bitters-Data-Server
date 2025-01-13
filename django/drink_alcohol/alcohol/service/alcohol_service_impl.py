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

            # whiskey
            cls.__instance.__whiskeyRepository = WhiskeyRepositoryImpl.getInstance()
            cls.__instance.__whiskeyPriceRepository = WhiskeyPriceRepositoryImpl.getInstance()
            cls.__instance.__whiskeyImageRepository = WhiskeyImageRepositoryImpl.getInstance()

            # wine
            cls.__instance.__wineRepository = WineRepositoryImpl.getInstance()
            cls.__instance.__winePriceRepository = WinePriceRepositoryImpl.getInstance()
            cls.__instance.__wineImageRepository = WineImageRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def requestAlcoholList(self, page, perPage):
        return self.__alcoholRepository.list(page, perPage)

    def createAlcohol(self, title, price, type, image):

        if type == RoleType.BEER.value:
            # if alcohol["type"] == RoleType.BEER.value:
            with transaction.atomic():
                #savedTypeBeer = self.__beerRepository.letRoleTypeBeer()
                savedBeer = self.__beerRepository.create(title, type="BEER")#savedTypeBeer)
                self.__beerPriceRepository.create(savedBeer, price)
                self.__beerImageRepository.create(savedBeer, image)

        if type == RoleType.WHISKEY.value:
            with transaction.atomic():
                savedTypeWhiskey = self.__whiskeyRepository.letRoleTypeWhiskey()
                savedWhiskey = self.__whiskeyRepository.create(title, savedTypeWhiskey)
                self.__whiskeyPriceRepository.create(savedWhiskey, price)
                self.__whiskeyImageRepository.create(savedWhiskey, image)

        if type == RoleType.WINE.value:
            with transaction.atomic():
                savedTypeWine = self.__wineRepository.letRoleTypeWine()
                savedWine = self.__wineRepository.create(title, savedTypeWine)
                self.__winePriceRepository.create(savedWine, price)
                self.__wineImageRepository.create(savedWine, image)

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