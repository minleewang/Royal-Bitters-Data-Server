from django.db import transaction

from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from beer.entity.beer import Beer
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
            cls.__instance.__alcoholRepository =  AlcoholRepositoryImpl.getInstance()


        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def requestList(self, page, perPage):
        return self.__beerRepository.list(page, perPage)


    def createBeerInfo(self, title, price, description, image):
        #create(self, title, price, type, image)
        with transaction.atomic():
            # 이 부분은 가상의 형태를 표현한 것임
            savedAlcohol = self.__alcoholRepository.create(title, price,type, image)
            # savedAlchol
            beer = Beer(alcohol=savedAlcohol)
            savedBeer = self.__beerRepository.create(beer)

            self.__beerPriceRepository.create(savedBeer, price)
            self.__beerDescriptionRepository.create(savedBeer, description)
            self.__beerImageRepository.create(savedBeer, image)




    def readBeerInfo(self, id):
        with transaction.atomic():

            # 맥주 데이터 조회
            foundBeer = self.__beerRepository.findById(id)
            print(f"found Beer: {foundBeer}")

            # 가격 데이터 조회
            foundBeerPrice = self.__beerPriceRepository.findByBeer(foundBeer)
            # BeerPrice 테이블에서 Beer와 연결된 가격 데이터를 찾습니다.
            print(f"found Beer Price: {foundBeerPrice}")

            # 이미지 데이터 조회
            foundBeerImage = self.__beerImageRepository.findByBeer(foundBeer)
            # BeerImage 테이블에서 Beer와 연결된 이미지 데이터를 찾습니다.
            print(f"found Beer Image: {foundBeerImage}")

            # 설명 데이터 조회
            foundBeerDescription = self.__beerDescriptionRepository.findByBeer(
                foundBeer)
            print(f"found Beer Description: {foundBeerDescription}")



            readBeerInfo = {
                'id': foundBeer.alcohol.getAlcoholId(),
                'title': foundBeer.alcohol.title,
                'price': foundBeerPrice.getPrice(),
                'image': foundBeerImage.getImage(),
                'description': foundBeerDescription.getDescription(),
            }

            return readBeerInfo
