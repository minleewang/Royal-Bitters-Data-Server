from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from alcohol.entity.role_type import RoleType
from whiskey.entity import whiskey
from whiskey.entity.whiskey import Whiskey
from whiskey.entity.whiskey_image import WhiskeyImage
from whiskey.entity.whiskey_price import WhiskeyPrice
from whiskey.repository.whiskey_repository import WhiskeyRepository


class WhiskeyRepositoryImpl(WhiskeyRepository):

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

        priceSubQuery = WhiskeyPrice.objects.filter(whiskey=OuterRef('pk')).values('price')[:1]
        imageSubQuery = WhiskeyImage.objects.filter(whiskey=OuterRef('pk')).values('image')[:1]

        whiskeyList = Whiskey.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
        )

        paginator = Paginator(whiskeyList, perPage)

        try:
            paiginatedWhiskeyList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedWhiskeyList = paginator.page(1)
        except EmptyPage:
            paiginatedWhiskeyList = []

        paiginatedWhiskeyList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedWhiskeyList
        ]  # paiginatedWhiskeyList에 있는 것들 하나씩 출력

        print(f"Total items: {len(whiskeyList)}")
        print(f"Page items: {len(paiginatedWhiskeyList)}")

        return paiginatedWhiskeyList, paginator.num_pages
                                    # 데이터의 전체 항목을 페이지 크기로 나눈 뒤의 총 페이지 수를 반환


    # Beer 테이블에서 create/ title 정보로 저장
    def create(self, whiskey):
        whiskey.save()
        return whiskey
                # 자동 저장

    # 검색 기능
    def findById(self, id):
        return Whiskey.objects.get(id=id)

    def findAll(self):
        return Whiskey.objects.all()


    def letRoleTypeWhiskey(self):
        alcoholRoleTypeIsWiskey = Whiskey.objects.filter(
            alcohol__type=RoleType.WHISKEY.value  # Alcohol 테이블의 type 필드가 'BEER'인 데이터 필터링
        )
        return alcoholRoleTypeIsWiskey
