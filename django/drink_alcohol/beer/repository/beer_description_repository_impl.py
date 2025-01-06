from beer.entity.beer_description import BeerDescription
from beer.repository.beer_description_repository import BeerDescriptionRepository


class BeerDescriptionRepositoryImpl(BeerDescriptionRepository):
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

    def create(self, beer, description):

        return BeerDescription.objects.create(beer=beer, description=description)

    def findByBeer(self, beer):
        return BeerDescription.objects.get(beer=beer)


