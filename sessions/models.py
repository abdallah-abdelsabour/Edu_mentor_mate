from django.db import models
from tags.models import Tags
from accounts.models import Mentor
# Create your models here.


import datetime
from django.core.exceptions import ValidationError


class SessionDate(models.Model):
    datetime = models.DateTimeField(auto_now=False, unique=True)

    def save(self, *args, **kwargs):
        if self.datetime < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(SessionDate, self).save(*args, **kwargs)


class Session(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags, blank=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    deterioration = models.TimeField(auto_now=False, auto_now_add=False)
    available_dates = models.ManyToManyField(SessionDate)
    #created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    ended_at = models.DateTimeField(auto_now=False)
