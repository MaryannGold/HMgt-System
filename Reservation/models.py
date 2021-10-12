from django.db import models
from Hotel.models import RoomStatus
# from Customer.models import Reservation
from Account.models import UserInfo
# Create your models here.

PaymentType = (
    ('CreditCard', 'CreditCard'),
    ('Cash', 'Cash'),
)


# class Reservations(models.Model):
#     guest = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     check_In_Date = models.CharField(max_length=40)
#     check_Out_Date = models.CharField(max_length=40)
#     how_many_guests = models.CharField(max_length=10, null=True, blank=True)
#     additional_request = models.CharField(max_length=100, null=True, blank=True)
#     reservation_Date = models.DateTimeField(auto_now_add=True)
#     reserved_room = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
#     payment_type = models.CharField(choices=PaymentType, max_length=20)


class GuestReservation(models.Model):
    guest = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    check_In_Date = models.CharField(max_length=40)
    check_Out_Date = models.CharField(max_length=40)
    how_many_guests = models.CharField(max_length=10, null=True, blank=True)
    additional_request = models.CharField(max_length=100, null=True, blank=True)
    reservation_Date = models.DateTimeField(auto_now_add=True)
    reserved_room = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    payment_type = models.CharField(choices=PaymentType, max_length=20)
