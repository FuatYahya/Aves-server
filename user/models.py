from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=25)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=25)
    dob = models.DateField()
    registered_at = models.DateTimeField(auto_now_add=True, blank=True)
    balance = models.FloatField(default=0)
    likes_count = models.IntegerField(default=0)
    contents_count = models.IntegerField(default=0)