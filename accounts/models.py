from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (  # Correctly named as "USER_TYPE_CHOICES"
        ('FARMER', 'Farmer'),
        ('BUYER', 'Buyer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Reference the correct variable



