import uuid
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
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
        alcohol_type = getRequest.get("type", None)
        paginatedAlcoholList, totalPages = self.alcoholService.requestList(page, perPage, alcohol_type)
        return JsonResponse({
            "dataList": paginatedAlcoholList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)


    def requestAlcoholCreate(self, request):

        postRequest = request.data
        alcoholImage = request.FILES.get('alcoholImage')
        alcoholTitle = postRequest.get('alcoholTitle')
        alcoholPrice = postRequest.get('alcoholPrice')
        alcoholType = postRequest.get('alcoholType')

        print(f"alcoholImage: {alcoholImage}, "
              f"alcoholTitle: {alcoholTitle}, "
              f"alcoholPrice: {alcoholPrice}, "
              f"alcoholType: {alcoholType},")


        if not all([alcoholImage, alcoholTitle, alcoholPrice, alcoholType]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedAlcohol = self.alcoholService.createAlcoholList(
            title=alcoholTitle,
            price=int(alcoholPrice),  # 정수형 변환
            type=alcoholType,
            image=alcoholImage,
        )
        return JsonResponse({"data": savedAlcohol}, status=status.HTTP_200_OK)


    def requestAlcoholRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)
            print(f"requestAlcoholRead() -> pk: {pk}")
            readAlcoholInfo = self.alcoholService.readAlcohol(pk)
            return JsonResponse(readAlcoholInfo, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)