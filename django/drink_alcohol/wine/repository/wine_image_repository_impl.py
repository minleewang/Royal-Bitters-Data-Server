import os

from wine.entity.wine_image import WineImage
from wine.repository.wine_image_repository import WineImageRepository


class WineImageRepositoryImpl(WineImageRepository):
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

    def create(self, wine, image):
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

        return WineImage.objects.create(wine=wine, image=image)

    def findByWine(self, wine):
        return WineImage.objects.get(wine=wine)

