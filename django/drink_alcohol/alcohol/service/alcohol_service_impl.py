<<<<<<< Updated upstream
<<<<<<< Updated upstream
from django.db import transaction

from alcohol.repository.alcohol_image_repository_impl import AlcoholImageRepositoryImpl
from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from alcohol.service.alcohol_service import AlcoholService


class AlcoholServiceImpl(AlcoholService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()
            cls.__instance.__alcoholImageRepository = AlcoholImageRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def requestAlcoholList(self, page, perPage):
        return self.__alcoholRepository.list(page, perPage)
    # AlcoholRepository에 list 있어야 함

    def createAlcoholList(self, title, price, type, image):
        with transaction.atomic():
            savedAlcohol = self.__alcoholRepository.create(title, price, type)
            self.__alcoholImageRepository.create(savedAlcohol, image)
            # AlcoholImageRepository 에도 list 있어야함

    def readAlcoholById(self, id):
        with transaction.atomic():
            foundAlcohol = self.__alcoholRepository.findById(id) # alcoholRepository에 findById 해야함
            print(f"foundAlcohol: {foundAlcohol}")
            foundAlcoholImage = self.__alcoholImageRepository.findById(foundAlcohol)
            print(f"foundAlcoholImage: {foundAlcoholImage}")


            readAlcohol = {
                'id': foundAlcohol.getId(),
                'title': foundAlcohol.getTitle(),
                'price': foundAlcohol.getPrice(),
                'image': foundAlcoholImage.getImage(),
                'type': foundAlcohol.getType()
            }

            return readAlcohol


=======
=======
>>>>>>> Stashed changes
from abc import ABC, abstractmethod


class AlcoholStoreService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):
        pass

    @abstractmethod
    def createAlcoholInfo(self, title, price, description, image, alcoholCategory):
        pass

    @abstractmethod
    def readAlcoholInfo(self, id):
<<<<<<< Updated upstream
        pass
>>>>>>> Stashed changes
=======
        pass
>>>>>>> Stashed changes
