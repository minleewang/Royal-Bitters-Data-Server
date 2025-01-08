from django.urls import path, include
from rest_framework.routers import DefaultRouter

from alcohol.controller.alcohol_controller import AlcoholController

router = DefaultRouter()



router.register(r"alcohol",
                AlcoholController, basename='alcohol')

urlpatterns = [
    path('', include(router.urls)),
    path('alcohol-list',
         AlcoholController.as_view({ 'get': 'requestAlcoholList' }),
         name='주류 전체 리스트 요청'),
    path('alcohol-create',
          AlcoholController.as_view({ 'post': 'requestAlcoholCreate' }),
          name='주류 (통합) 상품 등록 요청'),
    path('alcohol-read/<int:pk>',
          AlcoholController.as_view({ 'get': 'requestAlcoholRead' }),
          name='주류 (통합) 정보 읽기 요청'),
]