from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Hotel.models import HotelProfile, Reception, RoomCategory, Room, RoomStatus, HotelPictures, RoomPictures
# Register your models here.
admin.site.register(HotelProfile)
admin.site.register(Reception)
admin.site.register(Room)
admin.site.register(RoomStatus)
admin.site.register(HotelPictures)
admin.site.register(RoomPictures)
admin.site.register(RoomCategory)
