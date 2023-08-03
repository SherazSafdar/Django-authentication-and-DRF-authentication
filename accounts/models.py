from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username
