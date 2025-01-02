from django.db import transaction

from alcohol_store.repository.alcohol_category_repository_impl import AlcoholCategoryRepositoryImpl
from alcohol_store.repository.alcohol_description_repository_impl import AlcoholDescriptionRepositoryImpl
from alcohol_store.repository.alcohol_image_repository_impl import AlcoholImageRepositoryImpl
from alcohol_store.repository.alcohol_price_repository_impl import AlcoholPriceRepositoryImpl
from alcohol_store.service.alcohol_store_service import AlcoholStoreService
from alcohol_store.repository.alcohol_repository_impl import AlcoholRepositoryImpl


class AlcoholStoreServiceImpl(AlcoholStoreService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()
            cls.__instance.__alcoholPriceRepository = AlcoholPriceRepositoryImpl.getInstance()
            cls.__instance.__alcoholDescriptionRepository = AlcoholDescriptionRepositoryImpl.getInstance()
            cls.__instance.__alcoholImageRepository = AlcoholImageRepositoryImpl.getInstance()
            cls.__instance.__alcoholCategoryRepository = AlcoholCategoryRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 페이지네이션
    def requestList(self, page, perPage):
        return self.__alcoholRepository.list(page, perPage)

    # 상품의 전체 정보 등록하기
    def createAlcoholInfo(self, title, price, description, image, alcoholCategory):
        with transaction.atomic():
            savedAlcohol = self.__alcoholRepository.create(title)
            self.__alcoholPriceRepository.create(savedAlcohol, price)
            self.__alcoholDescriptionRepository.create(savedAlcohol, description)
            self.__alcoholImageRepository.create(savedAlcohol, image)
            self.__alcoholCategoryRepository.create(savedAlcohol, alcoholCategory)


    def readAlcoholInfo(self, id):
        with transaction.atomic():
            foundAlcohol = self.__alcoholRepository.findById(id)
            print(f"found Alcohol: {foundAlcohol}")
            foundAlcoholPrice = self.__alcoholPriceRepository.findByAlcohol(foundAlcohol)
            print(f"found Alcohol Price: {foundAlcoholPrice}")
            foundAlcoholImage = self.__alcoholImageRepository.findByAlcohol(foundAlcohol)
            print(f"found Alcohol Image: {foundAlcoholImage}")
            foundAlcoholDescription = self.__alcoholDescriptionRepository.findByAlcohol(
                foundAlcohol)
            print(f"found Alcohol Description: {foundAlcoholDescription}")
            foundAlcoholCategory = self.__alcoholCategoryRepository.findByAlcohol(
                foundAlcohol)
            print(f"found Alcohol Category: {foundAlcoholCategory}")


            readAlcoholInfo = {
                'id': foundAlcohol.getId(),
                'title': foundAlcohol.getTitle(),
                'price': foundAlcoholPrice.getPrice(),
                'image': foundAlcoholImage.getImage(),
                'description': foundAlcoholDescription.getDescription(),
                'category': foundAlcoholCategory.getCategory()
            }

            return readAlcoholInfo