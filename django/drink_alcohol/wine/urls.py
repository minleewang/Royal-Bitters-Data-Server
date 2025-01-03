from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wine.controller.wine_controller import WineController

router = DefaultRouter()



router.register(r"wine", WineController, basename='wine')

urlpatterns = [
    path('', include(router.urls)),
    path('wine-list',
         WineController.as_view({ 'get': 'requestWineList' }),
         name='와인 리스트 요청'),
    path('wine-create',
          WineController.as_view({ 'post': 'requestWineCreate' }),
          name='와인 상품 등록 요청'),
    path('wine-read/<int:pk>',
          WineController.as_view({ 'get': 'requestWineRead' }),
          name='와인 정보 읽기 요청'),
]