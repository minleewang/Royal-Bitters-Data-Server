import uuid
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl
from wine.service.wine_service_impl import WineServiceImpl


class WineController(viewsets.ViewSet):
    wineService = WineServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestWineList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedWineList, totalPages = self.wineService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedWineList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestWineCreate(self, request):
        postRequest = request.data

        wineImage = request.FILES.get('wineImage')
        wineTitle = postRequest.get('wineTitle')
        winePrice = postRequest.get('winePrice')
        wineDescription = postRequest.get('wineDescription')
        alcohol_type = 'WINE'

        print(f"wineImage: {wineImage}, "
              f"wineTitle: {wineTitle}, "
              f"winePrice: {winePrice}, "
              f"wineDescription: {wineDescription},",
              f"AlcoholType: {alcohol_type},")

        if not all([wineImage, wineTitle, winePrice, wineDescription]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedWine = self.wineService.createWineInfo(
            wineTitle,
            winePrice,
            wineDescription,
            wineImage
        )

        return JsonResponse({"data": savedWine}, status=status.HTTP_200_OK)

    def requestWineRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestWineRead() -> pk: {pk}")
            readWine = self.wineService.readWineInfo(pk)

            return JsonResponse(readWine, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)