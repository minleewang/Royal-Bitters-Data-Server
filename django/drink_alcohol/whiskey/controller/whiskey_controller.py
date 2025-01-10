import uuid
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK


from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl
from whiskey.service.whiskey_service_impl import WhiskeyServiceImpl


class WhiskeyController(viewsets.ViewSet):
    whiskeyService = WhiskeyServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestWhiskeyList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedWhiskeyList, totalPages = self.whiskeyService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedWhiskeyList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestWhiskeyCreate(self, request):
        postRequest = request.data

        whiskeyImage = request.FILES.get('whiskeyImage')
        whiskeyTitle = postRequest.get('whiskeyTitle')
        whiskeyPrice = postRequest.get('whiskeyPrice')
        whiskeyDescription = postRequest.get('whiskeyDescription')
        alcohol_type = 'WHISKEY'

        print(f"whiskeyImage: {whiskeyImage}, "
              f"whiskeyTitle: {whiskeyTitle}, "
              f"whiskeyPrice: {whiskeyPrice}, "
              f"whiskeyDescription: {whiskeyDescription},"
              f"AlcoholType: {alcohol_type}")

        if not all([whiskeyImage, whiskeyTitle, whiskeyPrice, whiskeyDescription]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedWhiskey = self.whiskeyService.createWhiskeyInfo(
            whiskeyTitle,
            whiskeyPrice,
            whiskeyDescription,
            whiskeyImage
        )

        return JsonResponse({"data": savedWhiskey}, status=status.HTTP_200_OK)

    def requestWhiskeyRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestWhiskeyRead() -> pk: {pk}")
            readWhiskey = self.whiskeyService.readWhiskeyInfo(pk)

            return JsonResponse(readWhiskey, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)