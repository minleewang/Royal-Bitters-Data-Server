from django.db import transaction

from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from wine.entity.wine import Wine
from wine.repository.wine_description_repository_impl import WineDescriptionRepositoryImpl
from wine.repository.wine_image_repository_impl import WineImageRepositoryImpl
from wine.repository.wine_price_repository_impl import WinePriceRepositoryImpl
from wine.repository.wine_repository_impl import WineRepositoryImpl
from wine.service.wine_service import WineService


class WineServiceImpl(WineService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__wineRepository = WineRepositoryImpl.getInstance()
            cls.__instance.__winePriceRepository = WinePriceRepositoryImpl.getInstance()
            cls.__instance.__wineDescriptionRepository = WineDescriptionRepositoryImpl.getInstance()
            cls.__instance.__wineImageRepository = WineImageRepositoryImpl.getInstance()
            cls.__instance.__alcoholRepository =  AlcoholRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 페이지네이션
    def requestList(self, page, perPage):
        return self.__wineRepository.list(page, perPage)

    # 상품의 전체 정보 등록하기
    def createWineInfo(self, title, price, description, image):
        with transaction.atomic():
            # 이 부분은 가상의 형태를 표현한 것임
            savedAlcohol = self.__alcoholRepository.create(title, price, type, image)
            # savedAlchol
            wine = Wine(alcohol=savedAlcohol)
            savedWine = self.__wineRepository.create(wine)

            self.__winePriceRepository.create(savedWine, price)
            self.__wineDescriptionRepository.create(savedWine, description)
            self.__wineImageRepository.create(savedWine, image)



    def readWineInfo(self, id):
        with transaction.atomic():
            foundWine = self.__wineRepository.findById(id)
            print(f"found Wine: {foundWine}")
            foundWinePrice = self.__winePriceRepository.findByWine(foundWine)
            print(f"found Wine Price: {foundWinePrice}")
            foundWineImage = self.__wineImageRepository.findByWine(foundWine)
            print(f"found Wine Image: {foundWineImage}")
            foundWineDescription = self.__wineDescriptionRepository.findByWine(
                foundWine)
            print(f"found Wine Description: {foundWineDescription}")



            readWineInfo = {
                'id': foundWine.alcohol.getAlcoholId(),
                'title': foundWine.alcohol.title,
                'price': foundWinePrice.getPrice(),
                'image': foundWineImage.getImage(),
                'description': foundWineDescription.getDescription(),
            }

            return readWineInfo