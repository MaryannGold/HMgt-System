from django.db import models
from Account.models import UserInfo
# from Reservation.models import Reservations
# Create your models here.


''''class CreditCard(models.Model):
    card_type = models.CharField(max_length=40)
    card_num = models.CharField(max_length=40)
    expiry_date = models.CharField(max_length=40)
    cvc = models.CharField(max_length=40)
    name_On_card = models.CharField(max_length=40)
    users = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True, blank=True)'''''


# class Ccard(models.Model):
#     card_type = models.CharField(max_length=20)
#     card_num = models.CharField(max_length=20)
#     expiry_Date = models.CharField(max_length=20)
#     cvc = models.CharField(max_length=5)
#     name_On_card = models.CharField(max_length=40)
#     transaction_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#
#
# class Payments(models.Model):
#     transaction_Date = models.DateTimeField(auto_now_add=True)
#     transaction_Amount = models.CharField(max_length=40)
#     current_Payment_Status = models.CharField(max_length=40)
#     reservations = models.ForeignKey(Reservations, on_delete=models.CASCADE)
#     creditcard = models.ForeignKey(Ccard, on_delete=models.CASCADE)
