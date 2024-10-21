from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


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
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'hotel_images', 'description', 'address', 'city', 'country']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer()
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_image', 'room', 'image_room/', 'description', 'address', 'city', 'country']

