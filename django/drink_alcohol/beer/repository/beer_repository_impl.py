from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from beer.entity.beer_image import BeerImage
from beer.entity.beer_price import BeerPrice
from beer.entity.beer import Beer
from beer.repository.beer_repository import BeerRepository


class BeerRepositoryImpl(BeerRepository):

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

        priceSubQuery = BeerPrice.objects.filter(Beer=OuterRef('pk')).values('price')[:1]
        imageSubQuery = BeerImage.objects.filter(Beer=OuterRef('pk')).values('image')[:1]

        BeerList = Beer.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
        )

        paginator = Paginator(BeerList, perPage)

        try:
            paiginatedBeerList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedBeerList = paginator.page(1)
        except EmptyPage:
            paiginatedBeerList = []

        paginatedBeerList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedBeerList
        ]  # paiginatedBeerList에 있는 것들 하나씩 출력

        print(f"Total items: {len(BeerList)}")
        print(f"Page items: {len(paiginatedBeerList)}")

        return paiginatedBeerList, paginator.num_pages
                                    # 데이터의 전체 항목을 페이지 크기로 나눈 뒤의 총 페이지 수를 반환


    # Beer 테이블에서 create/ title 정보로 저장
    def create(self, title):
        return Beer.objects.create(title=title)




    # 검색 기능
    def findById(self, id):
        return Beer.objects.get(id=id)

    def findAll(self):
        return Beer.objects.all()


