from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from alcohol.entity.alcohol import Alcohol
from alcohol.entity.role_type import RoleType
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
    def list(self, page, perPage):

        priceSubQuery = BeerPrice.objects.filter(beer=OuterRef('pk')).values('price')[:1]
        imageSubQuery = BeerImage.objects.filter(beer=OuterRef('pk')).values('image')[:1]
        #titleSubQuery = Beer.getAlcohol().object.filter(beer=OuterRef('pk')).values('type')[:1]
        titleSubQuery = Alcohol.objects.filter(beer_alcohols=OuterRef('pk')).values('title')[:1]

        beerList = Beer.objects.annotate(
            price=Coalesce(Subquery(priceSubQuery), Value(0)),
            image=Coalesce(Subquery(imageSubQuery), Value('')),
            title =Coalesce(Subquery(titleSubQuery), Value(''))
        )

        paginator = Paginator(beerList, perPage)

        try:
            paiginatedBeerList = paginator.page(page)
        except PageNotAnInteger:
            paiginatedBeerList = paginator.page(1)
        except EmptyPage:
            paiginatedBeerList = []

        paiginatedBeerList = [
            {
                'id': goods.id,
                'title': goods.title,
                'price': goods.price,
                'image': goods.image,
            }
            for goods in paiginatedBeerList
        ]  # paiginatedBeerList에 있는 것들 하나씩 출력

        print(f"Total items: {len(beerList)}")
        print(f"Page items: {len(paiginatedBeerList)}")

        return paiginatedBeerList, paginator.num_pages
                                    # 데이터의 전체 항목을 페이지 크기로 나눈 뒤의 총 페이지 수를 반환


    # Beer 테이블에서 create/ title 정보로 저장
    def create(self, beer):
        beer.save()
        return beer
                # 자동 저장

    # 검색 기능
    def findById(self, id):
        return Beer.objects.get(id=id)

    def findAll(self):
        return Beer.objects.all()

    def letRoleTypeBeer(self):

        alcoholRoleTypeIsBeer = Beer.objects.filter(
            alcohol__type=RoleType.BEER.value  # Alcohol 테이블의 type 필드가 'BEER'인 데이터 필터링
        )
        return alcoholRoleTypeIsBeer


        #try: # Beer 객체를 가져오면서 Alcohol 데이터도 가져옴
        #    beer = Beer.objects.select_related('alcohol').get(id=beer_id)
        #    return beer.alcohol.type

        #except Beer.DoesNotExist:
        #    raise Exception(f"Beer with ID {beer_id} does not exist.")

    #account = self.__accountRepository.findById(accountId)