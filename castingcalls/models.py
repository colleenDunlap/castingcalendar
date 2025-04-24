from django.db import models
from django.contrib.auth.models import User

class Casting(models.Model):
    title = models.CharField(max_length=200)
    producer = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    producer_name = models.CharField(max_length=200, null=True)
    production_company = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length = 1000)
    submission_due_date = models.DateTimeField()
    show_date = models.DateTimeField()
    submission_link = models.CharField(max_length=350, default = '')
    style = models.CharField(max_length=300, null=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        self.title
