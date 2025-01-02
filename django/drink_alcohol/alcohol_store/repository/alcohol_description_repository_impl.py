from alcohol_store.entity.alcohol_description import AlcoholDescription
from alcohol_store.repository.alcohol_description_repository import AlcoholDescriptionRepository



class AlcoholDescriptionRepositoryImpl(AlcoholDescriptionRepository):
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

    def create(self, alcohol, description):
        return AlcoholDescription.objects.create(alcohol=alcohol, description=description)

    def findByAlcohol(self, alcohol):
        return AlcoholDescription.objects.get(alcohol=alcohol)


