from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from alcohol.entity.alcohol import Alcohol
from alcohol.repository.alcohol_repository import AlcoholRepository


class AlcoholRepositoryImpl(AlcoholRepository):

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


    def list(self, page, perPage):

        alcoholList = Alcohol.objects.all()
        #alcoholList = Alcohol.objects.all()[(page - 1) * perPage:page * perPage]

        #paginator = Paginator(Alcohol, perPage)  # 이게 alcoholList 임의로 만들기 전 코드
        paginator = Paginator(alcoholList,perPage)

        try:
            paginatedAlcoholList = paginator.page(page)
        except PageNotAnInteger:
            paginatedAlcoholList = paginator.page(1)
        except EmptyPage:
            paginatedAlcoholList = []

        paginatedAlcoholList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
                'type': goods.type,
            }
            for goods in paginatedAlcoholList
        ]

        print(f"Total items: {len(alcoholList)}")
        print(f"Page items: {len(paginatedAlcoholList)}")

        return paginatedAlcoholList, paginator.num_pages


    def create(self, title, price, type, image):
        return Alcohol.objects.create(title=title, price=price, type=type, image=image)

    def findById(self, id):
        return Alcohol.objects.get(id=id)

    #def findAll(self):
    #    return Alcohol.objects.all()

    def findPriceById(self, id):
        alcoholPrice =  Alcohol.objects.get(id=id)
        return alcoholPrice.price

