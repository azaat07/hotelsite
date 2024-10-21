from django.urls import path
from .views import *

urlpatterns = [

    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='hotel_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='user_detail'),

    path('hotel/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('hotel/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='hotel_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='room_detail'),

    path('image_room/', ImageRoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='image_room_list'),
    path('image_room/<int:pk>/', ImageRoomViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='image_room_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='booking_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='rating_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='review_detail'),

]