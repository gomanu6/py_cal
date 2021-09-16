import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.task_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
