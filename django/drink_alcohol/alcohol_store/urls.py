from django.urls import path, include
from rest_framework.routers import DefaultRouter

from alcohol_store.controller.alcohol_store_controller import AlcoholStoreController

router = DefaultRouter()
router.register(r"alcohol-store", AlcoholStoreController, basename='alcohol-store')

urlpatterns = [
    path('', include(router.urls)),
    path('list/',
         AlcoholStoreController.as_view({ 'get': 'requestAlcoholList' }),
         name='주류 리스트 요청'),
    path('create/',
          AlcoholStoreController.as_view({ 'post': 'requestAlcoholCreate' }),
          name='주류 상품 등록 요청'),
    path('read/<int:pk>',
          AlcoholStoreController.as_view({ 'get': 'requestAlcoholRead' }),
          name='주류 정보 읽기 요청'),
]