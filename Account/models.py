from django.db import models
from django.contrib.auth.models import User

UserTypes = (
    ('Guest', 'Guest'),
    ('Receptionist', 'Receptionist'),
    ('Hotel Admin', 'Hotel Admin'),
)


class UserInfo(models.Model):
    address = models.CharField(max_length=200)
    telephoneNumber = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    dateRegistered = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=100, choices=UserTypes)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user

