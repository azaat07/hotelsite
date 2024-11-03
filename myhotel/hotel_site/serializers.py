from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class ImageRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_images = ImageRoomSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'room_price', 'room_images',
                  'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = ImageRoomSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'hotel_images', 'hotel_stars', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class HotelDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()


    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'country', 'city', 'address', 'hotel_stars', 'hotel_images',
                  'hotel_video', 'average_rating', 'reviews', 'created_date', 'owner', 'rooms']

    def get_average_rating(self, obj):
        return obj.get_average_rating()
