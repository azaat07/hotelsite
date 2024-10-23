from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age', 'phone_number', 'status']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel', 'hotel_image']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'capacity', 'price_per_night']


class ImageRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageRoom
        fields = ['id', 'room_image']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    status = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'description', 'address', 'city', 'country', 'status']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'rooms', 'hotel_image', 'description', 'address', 'city', 'country']

