import uuid
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from beer.service.beer_service_impl import BeerServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class BeerController(viewsets.ViewSet):
    beerService = BeerServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    # Pagination 페이지 나타내기
    def requestBeerList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
                                    # 총 8개씩 주류 표시
        paginatedBeerList, totalPages = self.beerService.requestList(page, perPage)
        print(f"paginatedBeerList: {paginatedBeerList}")

        return JsonResponse({
            "dataList": paginatedBeerList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)


    def requestBeerCreate(self, request):
        postRequest = request.data
        # post 방식으로 데이터 가져오기 (POST 데이터 추출)

        beerImage = request.FILES.get('beerImage')
        # 클라이언트가 업로드한 파일(beerImage)을 가져옵니다.이는 이미지와 같은 파일 데이터 처리를 담당.
        beerTitle = postRequest.get('beerTitle')
        beerPrice = postRequest.get('beerPrice')
        beerDescription = postRequest.get('beerDescription')
        alcohol_type = 'BEER'
        # POST 요청에서 클라이언트가 보낸 beerTitle, beerPrice, beerDescription 데이터를 추출

        print(f"BeerImage: {beerImage}, "
              f"BeerTitle: {beerTitle}, "
              f"BeerPrice: {beerPrice}, "
              f"BeerDescription: {beerDescription},"
              f"AlcoholType: {alcohol_type}")

        # 데이터 검증
        if not all([beerImage, beerTitle, beerPrice, beerDescription]):
            # 여기서는 beerImage, beerTitle, beerPrice, beerDescription 중 하나라도 없으면 오류 메시지를 반환.
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        # 데이터 생성
        savedBeer = self.beerService.createBeerInfo(
            beerTitle,
            beerPrice,
            beerDescription,
            beerImage
        )

        return JsonResponse({"data": savedBeer}, status=status.HTTP_200_OK)


    def requestBeerRead(self, request, pk=None):
        # pk=None은 함수가 호출될 때 pk 값을 반드시 전달하지 않아도 된다는 것을 의미합니다.
        # 만약 pk가 함수 호출 시 제공되지 않으면, 기본값으로 None이 사용됩니다.

        try:
            # 코드에서 if not pk:라는 검증 로직을 통해 pk 값이 없는 경우를 처리
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)
                # pk=None인 상태에서 함수가 실행되지 않도록, 클라이언트에 적절한 오류를 반환

            print(f"requestBeerRead() -> pk: {pk}")
            readBeer = self.beerService.readBeerInfo(pk)
            # 이 코드는 self.beerService 객체의 readBeerInfo 메서드를 호출하여 특정 맥주 데이터를 조회하는 역할을 합니다.
            # 전달된 pk(Primary Key, ID)를 기반으로 해당 맥주의 데이터를 가져오고, 이를 readBeer 변수에 저장합니다

            return JsonResponse(readBeer, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)