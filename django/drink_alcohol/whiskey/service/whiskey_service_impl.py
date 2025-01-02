from django.db import transaction

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
            savedWhiskey = self.__whiskeyRepository.create(title)
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
                'id': foundWhiskey.getId(),
                'title': foundWhiskey.getTitle(),
                'price': foundWhiskeyPrice.getPrice(),
                'image': foundWhiskeyImage.getImage(),
                'description': foundWhiskeyDescription.getDescription(),
            }

            return readWhiskeyInfo