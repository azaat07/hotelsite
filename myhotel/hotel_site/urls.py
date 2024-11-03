from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'hotels', HotelListViewSet, basename='hotels-list')
router.register(r'rooms', RoomListViewSet, basename='rooms-list')


urlpatterns = [
    path('', include(router.urls))
]