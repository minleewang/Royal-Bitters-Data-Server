from django.db import transaction

from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from whiskey.entity.whiskey import Whiskey
from whiskey.repository.whiskey_description_repository_impl import WhiskeyDescriptionRepositoryImpl
from whiskey.repository.whiskey_image_repository_impl import WhiskeyImageRepositoryImpl
from whiskey.repository.whiskey_price_repository_impl import WhiskeyPriceRepositoryImpl
from whiskey.repository.whiskey_repository_impl import WhiskeyRepositoryImpl
from whiskey.service.whiskey_service import WhiskeyService


class WhiskeyServiceImpl(WhiskeyService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__whiskeyRepository = WhiskeyRepositoryImpl.getInstance()
            cls.__instance.__whiskeyPriceRepository = WhiskeyPriceRepositoryImpl.getInstance()
            cls.__instance.__whiskeyDescriptionRepository = WhiskeyDescriptionRepositoryImpl.getInstance()
            cls.__instance.__whiskeyImageRepository = WhiskeyImageRepositoryImpl.getInstance()
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 페이지네이션
    def requestList(self, page, perPage):
        return self.__whiskeyRepository.list(page, perPage)


    # 상품의 전체 정보 등록하기
    def createWhiskeyInfo(self, title, price, description, image):
        with transaction.atomic():
            # 이 부분은 가상의 형태를 표현한 것임
            savedAlcohol = self.__alcoholRepository.create(title, price, type, image)
            # savedAlchol
            whiskey = Whiskey(alcohol=savedAlcohol)
            savedWhiskey = self.__whiskeyRepository.create(whiskey)

            self.__whiskeyPriceRepository.create(savedWhiskey, price)
            self.__whiskeyDescriptionRepository.create(savedWhiskey, description)
            self.__whiskeyImageRepository.create(savedWhiskey, image)


    def readWhiskeyInfo(self, id):
        with transaction.atomic():

            foundWhiskey = self.__whiskeyRepository.findById(id)
            print(f"found Whiskey: {foundWhiskey}")

            foundWhiskeyPrice = self.__whiskeyPriceRepository.findByWhiskey(foundWhiskey)
            print(f"found Whiskey Price: {foundWhiskeyPrice}")

            foundWhiskeyImage = self.__whiskeyImageRepository.findByWhiskey(foundWhiskey)
            print(f"found Whiskey Image: {foundWhiskeyImage}")

            foundWhiskeyDescription = self.__whiskeyDescriptionRepository.findByWhiskey(
                foundWhiskey)
            print(f"found Whiskey Description: {foundWhiskeyDescription}")



            readWhiskeyInfo = {
                'id': foundWhiskey.alcohol.getAlcoholId(),
                'title': foundWhiskey.alcohol.title,
                'price': foundWhiskeyPrice.getPrice(),
                'image': foundWhiskeyImage.getImage(),
                'description': foundWhiskeyDescription.getDescription(),
            }

            return readWhiskeyInfo
