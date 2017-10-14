"Sual User Model"

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    "User Model"
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company = models.CharField(max_length=100, blank=True, verbose_name="Company")
    tittle = models.CharField(max_length=100, blank=True, verbose_name="Tittle")

    def __str__(self):
        return "%s" % (self.user)
