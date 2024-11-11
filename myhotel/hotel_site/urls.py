from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'hotels_list', HotelListViewSet, basename='hotels-list')
router.register(r'hotels_detail', HotelDetailViewSet, basename='hotels_detail')
router.register(r'rooms', RoomListViewSet, basename='rooms-list')
router.register(r'room-detail', RoomDetailViewSet, basename='hotels-detail')
router.register(r'Booking', BookingViewSet, basename='booking')
router.register(r'review', ReviewViewSet, basename='Review')


urlpatterns = [
    path('', include(router.urls))
]