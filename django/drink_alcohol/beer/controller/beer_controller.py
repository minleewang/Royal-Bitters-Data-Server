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

    def requestBeerList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedBeerList, totalPages = self.beerService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedBeerList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestBeerCreate(self, request):
        postRequest = request.data

        beerImage = request.FILES.get('beerImage')
        beerTitle = postRequest.get('beerTitle')
        beerPrice = postRequest.get('beerPrice')
        beerDescription = postRequest.get('beerDescription')
        print(f"BeerImage: {beerImage}, "
              f"BeerTitle: {beerTitle}, "
              f"BeerPrice: {beerPrice}, "
              f"BeerDescription: {beerDescription},")

        if not all([beerImage, beerTitle, beerPrice, beerDescription]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedBeer = self.beerService.createBeerInfo(
            beerTitle,
            beerPrice,
            beerDescription,
            beerImage
        )

        return JsonResponse({"data": savedBeer}, status=status.HTTP_200_OK)

    def requestBeerRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestBeerRead() -> pk: {pk}")
            readBeer = self.beerService.readBeerInfo(pk)

            return JsonResponse(readBeer, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)