from django.db import models
from django.contrib.auth.models import User

class Casting(models.Model):
    title = models.CharField(max_length=200)
    producer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    producer_name = models.CharField(max_length=200,null=True, blank=True)
    production_company = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length = 1000)
    submission_due_date = models.DateTimeField()
    show_date = models.DateTimeField()
    submission_link = models.CharField(max_length=350)
    style = models.CharField(max_length=300, null=True)
    is_published = models.BooleanField(default = False)
    def __str__(self):
        return self.title

class Calendar(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class CalendarItem(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=350)
    casting = models.ForeignKey(Casting, on_delete=models.SET_NULL, null=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, default=None)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
