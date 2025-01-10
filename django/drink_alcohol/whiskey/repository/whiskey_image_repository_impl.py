import os

from whiskey.entity.whiskey_image import WhiskeyImage
from whiskey.repository.whiskey_image_repository import WhiskeyImageRepository


class WhiskeyImageRepositoryImpl(WhiskeyImageRepository):
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

    def create(self, whiskey, image):
        print(f"current working directory: {os.getcwd()}")
        uploadDirectory = os.path.join('../../../../SecondProject/ui/assets/images/uploadImages채ㅜㅇㅁ ㅁㅊ샾ㅁㅅㄷ 나ㅜ08-312'
                                       '')
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, image.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        return WhiskeyImage.objects.create(whiskey=whiskey, image=image)

    def findByWhiskey(self, whiskey):
        return WhiskeyImage.objects.get(whiskey=whiskey)

