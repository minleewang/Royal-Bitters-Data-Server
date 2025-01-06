from django.urls import path, include
from rest_framework.routers import DefaultRouter

from beer.controller.beer_controller import BeerController

router = DefaultRouter()

router.register(r"beer", BeerController, basename='beer')

urlpatterns = [
    path('', include(router.urls)),
    path('beer-list',
         BeerController.as_view({ 'get': 'requestBeerList' }),
         name='맥주 리스트 요청'),
    path('beer-create',
          BeerController.as_view({ 'post': 'requestBeerCreate' }),
          name='맥주 상품 등록 요청'),
    path('beer-read/<int:pk>',
          BeerController.as_view({ 'get': 'requestBeerRead' }),
          name='맥주 정보 읽기 요청'),
]