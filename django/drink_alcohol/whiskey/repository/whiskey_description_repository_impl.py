from whiskey.entity.whiskey_description import WhiskeyDescription
from whiskey.repository.whiskey_description_repository import WhiskeyDescriptionRepository


class WhiskeyDescriptionRepositoryImpl(WhiskeyDescriptionRepository):
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

    def create(self, whiskey, description):
        return WhiskeyDescription.objects.create(whiskey=whiskey, description=description)

    def findByWhiskey(self, whiskey):
        return WhiskeyDescription.objects.get(whiskey=whiskey)


