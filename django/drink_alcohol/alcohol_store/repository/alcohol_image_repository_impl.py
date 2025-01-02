import os

from alcohol_store.entity.alcohol_image import AlcoholImage
from alcohol_store.repository.alcohol_image_repository import AlcoholImageRepository


class AlcoholImageRepositoryImpl(AlcoholImageRepository):
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

    def create(self, alcohol, image):
        print(f"current working directory: {os.getcwd()}")
        uploadDirectory = os.path.join('../../../nuxt/notes/ui/assets/images/uploadImages')
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, image.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        return AlcoholImage.objects.create(alcohol=alcohol, image=image)

    def findByAlcohol(self, alcohol):
        return AlcoholImage.objects.get(alcohol=alcohol)

