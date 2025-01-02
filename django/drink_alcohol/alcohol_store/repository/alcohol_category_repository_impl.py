from alcohol_store.entity.alcohol_store_category import AlcoholCategory
from alcohol_store.repository.alcohol_category_repository import AlcoholCategoryRepository


class AlcoholCategoryRepositoryImpl(AlcoholCategoryRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, alcohol, alcoholCategory):
        return AlcoholCategory.objects.create(alcohol=alcohol, alcoholCategory=alcoholCategory)

    def findByAlcohol(self, alcohol):
        return AlcoholCategory.objects.get(alcohol=alcohol)