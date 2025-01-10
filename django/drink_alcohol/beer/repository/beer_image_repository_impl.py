import os

from beer.entity.beer_image import BeerImage
from beer.repository.beer_image_repository import BeerImageRepository


class BeerImageRepositoryImpl(BeerImageRepository):
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

    def create(self, beer, image):
        print(f"current working directory: {os.getcwd()}")
        uploadDirectory = os.path.join('../../../../SecondProject/ui/assets/images/uploadImages')
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, image.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        return BeerImage.objects.create(beer=beer, image=image)

    def findByBeer(self, beer):
        return BeerImage.objects.get(beer=beer)

