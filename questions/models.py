"Questions App"

from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    user = models.ForeignKey(User)
    body = models.CharField(max_length=140, blank=True, verbose_name="Tittle")

    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)


    def __str__(self):
        return "%s" % (self.body)
