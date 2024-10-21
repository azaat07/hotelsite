from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(95)])
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    STATUS_CHOICE = (
        ('клиент', 'Клиент'),
        ('владелец', 'Владелец'),
        ('Админ', 'Админ'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='simple')

    def __str__(self):
        return f' {self.first_name} - {self.last_name} '


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    def str(self):
        return f'{self.name_hotel} - {self.country}'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.SmallIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    price_per_night = models.PositiveIntegerField()

    def str(self):
        return f'{self.room_number}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')


class Booking(models.Model):
    user = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('Бронь', 'Бронь'),
        ('Свободный', 'Свободный'),
        ('Занят', 'Занят')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
