"Questions App"

from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    "Questions Model"
    user = models.ForeignKey(User)
    body = models.CharField(max_length=140, verbose_name="Tittle")

    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)


    def __str__(self):
        return "%s" % (self.body)


class Answers(models.Model):
    "Answers Model"
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    body = models.TextField(max_length=3000, blank=True, verbose_name="Body")
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)

    def __str__(self):
        return "%s" % (self.body)
