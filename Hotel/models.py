from django.db import models
from Account.models import UserInfo
from django.conf import settings

CATEGORY_CHOICES = (
    ('lagos', 'LAGOS'),
    ('abuja', 'Abuja'),
    ('owerri', 'OWERRI'),
    ('portharcourt', 'PORTHARCOURT'),
    ('delta', 'DELTA'),
    ('calabar', 'CALABAR'),
    ('uyo', 'UYO'),
    ('enugu', 'ENUGU'),
    ('owerri', 'OWERRI'),
    ('kano', 'KANO'),
)


class HotelProfile(models.Model):
    admin = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=200, null=True)
    # hotel_logistics = models.CharField(max_length=100)
    hotel_contact = models.CharField(max_length=20, null=True)
    brief_description = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='select state')

    def __str__(self):
        return self.hotel_name


class Reception(models.Model):
    reception = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    hotel = models.ForeignKey(HotelProfile, on_delete=models.CASCADE)


class Room(models.Model):
    room_type = models.ForeignKey('Hotel.RoomCategory', on_delete=models.CASCADE, null=True, blank=True)
    # room_rate = models.CharField(max_length=200, null=True, blank=True)
    room_description = models.CharField(max_length=200, null=True, blank=True)
    room_bed_type = models.CharField(max_length=25)
    room_number = models.CharField(max_length=25, null=True, blank=True)
    hotel = models.ForeignKey(HotelProfile, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s: %s' % (self.hotel, self.room_type)


class RoomCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_descriptions = models.CharField(max_length=500)
    room_rate = models.CharField(max_length=200, null=True, blank=True)
    admin = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(HotelProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
         return u'%s:  %s' % (self.admin, self.category_name)


room_status = (
    ('Available', 'Available'),
    ('Occupied', 'Occupied'),
)


class RoomStatus(models.Model):
    occupationStatus = models.CharField(max_length=40, choices=room_status)
    starting_Date = models.DateTimeField()
    ending_Date = models.DateTimeField()
    status_UpdateTime = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class HotelPictures(models.Model):
    picture_Date = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=100, null=True)
    hotel = models.ForeignKey(HotelProfile, on_delete=models.CASCADE)
    hotel_image = models.FileField(upload_to='Hotel/Hotel/Pictures/', null=True)

    def __str__(self):
        return u'%s - %s' % (self.hotel.hotel_name, self.image_name)


class RoomPictures(models.Model):
    picture_Date = models.DateTimeField(auto_now_add=True)
    roomcategory = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, null=True, blank=True)
    room_image_name = models.CharField(max_length=50, null=True, blank=True)
    room_image = models.FileField(upload_to='Hotel/Room/Pictures/')








