"Sual Up-Topic Model"

from django.db import models
from django.contrib.auth.models import User

from questions.models import Answers, Questions


class Topic(models.Model):
    "Topic Model"
    name = models.CharField(max_length=100, blank=False, verbose_name="Topic Name")
    tittle = models.CharField(max_length=100, blank=True, verbose_name="Tittle")
    about = models.CharField(max_length=250, blank=True, verbose_name="About Topic")
    image = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return "%s" % (self.name)


class Vote_Answer(models.Model):
    "Answer up vote"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # True is UpVote and False DownVote
    type = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.answer)

    class Meta:
        unique_together = ('user', 'answer',)

class Topic_Questions(models.Model):
    "Questions in Topic data"
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.topic, self.questions)
