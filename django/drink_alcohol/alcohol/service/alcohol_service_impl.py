from django.db import transaction

from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from alcohol.service.alcohol_service import AlcoholService

# 기본적으로 Alcohol 데이터를 생성, 읽기, 수정, 삭제하는 기능이 필요
# 수정, 삭제는 안하기로 Create,Read 이 두개만 합시다.

class AlcoholServiceImpl(AlcoholService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def requestAlcoholList(self, page, perPage):
        return self.__alcoholRepository.list(page, perPage)


    def createAlcohol(self, title, price, type, image):
        #with transaction.atomic():
        return self.__alcoholRepository.create(title, price, type, image)


    # 이 부분 수정 필요
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