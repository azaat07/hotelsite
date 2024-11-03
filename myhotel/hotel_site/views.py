from rest_framework import viewsets, permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HotelFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .permission import CheckOwner, CheckCRUD


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['name_hotel']
    ordering_fields = ['price_per_night']
    permission_classes = [CheckCRUD]


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    permission_classes = [CheckCRUD]


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [CheckCRUD]


class ImageRoomViewSet(viewsets.ModelViewSet):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, CheckOwner]