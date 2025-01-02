from wine.entity.wine_description import WineDescription
from wine.repository.wine_description_repository import WineDescriptionRepository


class WineDescriptionRepositoryImpl(WineDescriptionRepository):
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

    def create(self, wine, description):
        return WineDescription.objects.create(wine=wine, description=description)

    def findByWine(self, wine):
        return WineDescription.objects.get(wine=wine)


