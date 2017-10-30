"Answers Model"

from django.db import models
from django.contrib.auth.models import User

from questions.models import Questions

class Answers(models.Model):
    "Answers Model"
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    body = models.TextField(max_length=300, blank=True, verbose_name="Company")

    def __str__(self):
        return "%s" % (self.question)