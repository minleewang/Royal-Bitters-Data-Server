from django.db import transaction

from beer.repository.beer_description_repository_impl import BeerDescriptionRepositoryImpl
from beer.repository.beer_image_repository_impl import BeerImageRepositoryImpl
from beer.repository.beer_price_repository_impl import BeerPriceRepositoryImpl
from beer.repository.beer_repository_impl import BeerRepositoryImpl
from beer.service.beer_service import BeerService


class BeerServiceImpl(BeerService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__beerRepository = BeerRepositoryImpl.getInstance()
            cls.__instance.__beerPriceRepository = BeerPriceRepositoryImpl.getInstance()
            cls.__instance.__beerDescriptionRepository = BeerDescriptionRepositoryImpl.getInstance()
            cls.__instance.__beerImageRepository = BeerImageRepositoryImpl.getInstance()


        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 페이지네이션
    def requestList(self, page, perPage):
        return self.__beerRepository.list(page, perPage)

    # 상품의 전체 정보 등록하기
    def createBeerInfo(self, title, price, description, image):
        with transaction.atomic():
            savedBeer = self.__beerRepository.create(title)
            self.__beerPriceRepository.create(savedBeer, price)
            self.__beerDescriptionRepository.create(savedBeer, description)
            self.__beerImageRepository.create(savedBeer, image)



    def readBeerInfo(self, id):
        with transaction.atomic():
            foundBeer = self.__beerRepository.findById(id)
            print(f"found Beer: {foundBeer}")
            foundBeerPrice = self.__beerPriceRepository.findByBeer(foundBeer)
            print(f"found Beer Price: {foundBeerPrice}")
            foundBeerImage = self.__beerImageRepository.findByBeer(foundBeer)
            print(f"found Beer Image: {foundBeerImage}")
            foundBeerDescription = self.__beerDescriptionRepository.findByBeer(
                foundBeer)
            print(f"found Beer Description: {foundBeerDescription}")



            readBeerInfo = {
                'id': foundBeer.getId(),
                'title': foundBeer.getTitle(),
                'price': foundBeerPrice.getPrice(),
                'image': foundBeerImage.getImage(),
                'description': foundBeerDescription.getDescription(),
            }

            return readBeerInfo