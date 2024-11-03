from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser,  Group, Permission


class UserProfile(AbstractUser):
    # Добавляем related_name, чтобы устранить конфликты
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )
    ROLE_CHOICE = (
        ('simpleUser', 'simpleUser'),
        ('ownerUser', 'ownerUser'),
    )
    user_role = models.CharField(max_length=10, choices=ROLE_CHOICE, default='simpleUser')
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(95)])
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.hotel_name}, {self.country}, {self.city}'

    def get_average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_image = models.ImageField(upload_to='hotel_image/')



class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),
    )
    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('свободен', 'Свободен'),
        ('забронирован', 'Забронирован'),
        ('занят', 'Занят'),
    )
    room_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()

    def str(self):
        return f'{self.hotel_room}, {self.room_number}, {self.room_type}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_image = models.ImageField(upload_to='room_image/')


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подвеждено', 'подвеждено'),
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.user_book}, {self.hotel_book}, {self.room_book}, {self.status_book}'


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user_name} - {self.hotel}, {self.stars}'
