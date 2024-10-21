from django.contrib import admin
from.models import *


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline]


admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(ImageRoom)
admin.site.register(Booking)
admin.site.register(Rating)
admin.site.register(Review)

