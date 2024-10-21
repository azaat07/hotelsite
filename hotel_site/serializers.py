from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ImageRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = '__all__'


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
    class Meta:
        model = Car
        fields = ['id', 'hotel_name', 'hotel_image', 'description', 'address', 'city', 'country']


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['hotel_name', 'hotel_image', 'room', 'image_room', 'description', 'address', 'city', 'country']

