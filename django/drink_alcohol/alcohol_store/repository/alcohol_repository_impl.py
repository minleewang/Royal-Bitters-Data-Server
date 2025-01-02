from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from alcohol_store.entity.alcohol import Alcohol
from alcohol_store.entity.alcohol_image import AlcoholImage
from alcohol_store.entity.alcohol_price import AlcoholPrice
from alcohol_store.repository.alcohol_repository import AlcoholRepository


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

    # 여기서 페이지 네이션 동작 구현
    def list(self, page=1, perPage=10): # perPage 몇개로 설정해야 하는지 몰라서 일단 10개

        priceSubQuery = AlcoholPrice.objects.filter(alcohol=OuterRef('pk')).values('price')[:1]
        imageSubQuery = AlcoholImage.objects.filter(alcohol=OuterRef('pk')).values('image')[:1]

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

        paginatedAlcoholList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedAlcoholList
        ]  # paiginatedAlcoholList에 있는 것들 하나씩 출력

        print(f"Total items: {len(alcoholList)}")
        print(f"Page items: {len(paiginatedAlcoholList)}")

        return paiginatedAlcoholList, paginator.num_pages
                                    # 데이터의 전체 항목을 페이지 크기로 나눈 뒤의 총 페이지 수를 반환


    # alcohol 테이블에서 create/ title 정보로 저장
    def create(self, title):
        return Alcohol.objects.create(title=title)





