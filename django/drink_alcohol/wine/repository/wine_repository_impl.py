from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType
from wine.entity.wine import Wine
from wine.entity.wine_image import WineImage
from wine.entity.wine_price import WinePrice
from wine.repository.wine_repository import WineRepository


class WineRepositoryImpl(WineRepository):

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

        priceSubQuery = WinePrice.objects.filter(wine=OuterRef('pk')).values('price')[:1]
        imageSubQuery = WineImage.objects.filter(wine=OuterRef('pk')).values('image')[:1]
        titleSubQuery = Alcohol.objects.filter(wine_alcohols=OuterRef('pk')).values('title')[:1]

        wineList = Wine.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
            title=Coalesce(Subquery(titleSubQuery), Value(''))
        )

        paginator = Paginator(wineList, perPage)

        try:
            paiginatedWineList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedWineList = paginator.page(1)
        except EmptyPage:
            paiginatedWineList = []

        paiginatedWineList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedWineList
        ]  # paiginatedWineList에 있는 것들 하나씩 출력

        print(f"Total items: {len(wineList)}")
        print(f"Page items: {len(paiginatedWineList)}")

        return paiginatedWineList, paginator.num_pages
                                    # 데이터의 전체 항목을 페이지 크기로 나눈 뒤의 총 페이지 수를 반환

        # Beer 테이블에서 create/ title 정보로 저장
    def create(self, wine):
        wine.save()
        return wine
        # 자동 저장

    # 검색 기능
    def findById(self, id):
        return Wine.objects.get(id=id)

    def findAll(self):
        return Wine.objects.all()


    def letRoleTypeWine(self):
        alcoholRoleTypeIsWine = Wine.objects.filter(
            alcohol__type=RoleType.WINE.value  # Alcohol 테이블의 type 필드가 'BEER'인 데이터 필터링
        )
        return alcoholRoleTypeIsWine

