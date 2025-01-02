import uuid

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from alcohol_store.service.alcohol_store_service_impl import AlcoholStoreServiceImpl
#from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl

# 프론트에 보낼 정보들 여기서 정의

class AlcoholStoreController(viewsets.ViewSet):
    alcoholStoreService = AlcoholStoreServiceImpl.getInstance()
    #redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestAlcoholList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedAlcoholList, totalPages = self.alcoholStoreService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedAlcoholList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestAlcoholCreate(self, request):
        postRequest = request.data

        alcoholImage = request.FILES.get('alcoholImage')
        alcoholTitle = postRequest.get('alcoholTitle')
        alcoholPrice = postRequest.get('alcoholPrice')
        alcoholDescription = postRequest.get('alcoholDescription')
        alcoholCategory = postRequest.get('alcoholCategory')
        print(f"alcoholImage: {alcoholImage}, "
              f"alcoholTitle: {alcoholTitle}, "
              f"alcoholPrice: {alcoholPrice}, "
              f"alcoholDescription: {alcoholDescription},"
              f"alcoholCategory: {alcoholCategory}")

        if not all([alcoholImage, alcoholTitle, alcoholPrice, alcoholDescription, alcoholCategory]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedAlcohol = self.alcoholStoreService.createAlcoholInfo(
            alcoholTitle,
            alcoholPrice,
            alcoholDescription,
            alcoholImage,
            alcoholCategory,
        )

        return JsonResponse({"data": savedAlcohol}, status=status.HTTP_200_OK)

    def requestAlcoholRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestAlcoholRead() -> pk: {pk}")
            readAlcohol = self.alcoholStoreService.readAlcoholInfo(pk)

            return JsonResponse(readAlcohol, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)