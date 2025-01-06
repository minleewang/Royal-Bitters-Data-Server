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


    def list(self, page=1, perPage=10):
#   실제 GameSoftwarePrice에 gameSoftare에 해당하는 pk 값 중 price 값과 일치되는 것을 뽑아옴
# ???? 난 price가 없는데
        priceSubQuery = Alcohol.objects.filter(alcohol=OuterRef('pk')).values('price')[:1]
        imageSubQuery = AlcoholImage.objects.filter(beer=OuterRef('pk')).values('image')[:1]

        alcoholList = Alcohol.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
        )

        paginator = Paginator(alcoholList, perPage)

        try:
            paiginatedAlcoholList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedAlcoholList = paginator.page(1)
        except EmptyPage:
            paiginatedAlcoholList = []

        paiginatedAlcoholList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedAlcoholList
        ]  # paiginatedBeerList에 있는 것들 하나씩 출력

        print(f"Total items: {len(alcoholList)}")
        print(f"Page items: {len(paiginatedAlcoholList)}")

        return paiginatedAlcoholList, paginator.num_pages



    # Beer 테이블에서 create/ title 정보로 저장
    def create(self, title):
        return Alcohol.objects.create(title=title)




    # 검색 기능
    def findById(self, id):
        return Alcohol.objects.get(id=id)

    def findAll(self):
        return Alcohol.objects.all()