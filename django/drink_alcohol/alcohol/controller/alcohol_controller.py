import uuid

from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from alcohol.entity import alcohol
from alcohol.service.alcohol_service_impl import AlcoholServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class AlcoholController(viewsets.ViewSet):
    alcoholService = AlcoholServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestAlcoholList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedAlcoholList, totalPages = self.alcoholService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedAlcoholList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestAlcoholCreate(self, request):
        postRequest = request.data

    # title, price, type
        alcoholImage = request.FILES.get('alcoholImage')
        alcohol.title = postRequest.get('alcoholTitle')
        alcohol.price = postRequest.get('alcoholPrice')
        alcohol.role = postRequest.get('alcoholType')

        print(f"alcoholImage: {alcoholImage}, "
              f"alcoholTitle: {alcohol.title}, "
              f"alcoholPrice: {alcohol.price}, "
              f"alcoholCategory: {alcohol.role}")

        if not all([alcoholImage, alcohol.title, alcohol.price, alcohol.role]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedAlcohol = self.alcoholService.createAlcoholList(
            alcohol.title,
            alcohol.price,
            alcohol.role,
            alcoholImage
        )

        return JsonResponse({"data": savedAlcohol}, status=status.HTTP_200_OK)

    def requestAlcoholRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestGameSoftwareRead() -> pk: {pk}")
            readAlcohol = self.alcoholService.readAlcoholById(pk)

            return JsonResponse(readAlcohol, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)