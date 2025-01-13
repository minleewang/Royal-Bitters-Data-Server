from django.urls import path, include
from rest_framework.routers import DefaultRouter

from whiskey.controller.whiskey_controller import WhiskeyController

router = DefaultRouter()



router.register(r"whiskey", WhiskeyController, basename='whiskey')

urlpatterns = [
    path('', include(router.urls)),
    path('whiskey-list',
         WhiskeyController.as_view({ 'get': 'requestWhiskeyList' }),
         name='위스키 리스트 요청'),
    path('whiskey-create',
          WhiskeyController.as_view({ 'post': 'requestWhiskeyCreate' }),
          name='위스키 상품 등록 요청'),
    path('whiskey-read/<int:pk>',
          WhiskeyController.as_view({ 'get': 'requestWhiskeyRead' }),
          name='위스키 정보 읽기 요청'),
]