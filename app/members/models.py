from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_img = models.ImageField(upload_to='user_profile')

    def __str__(self):
        return self.username