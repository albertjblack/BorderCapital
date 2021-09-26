from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model

# Create your models here.

class Customer(auth_models.User, auth_models.PermissionsMixin):
    customer_type = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.png')
    def __str__(self):
        return "@{}".format(self.username)

