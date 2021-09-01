from django.db import models
from user.models import User


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    key = models.CharField(max_length=16)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.FloatField(default=0)
    likes_count = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    discription = models.TextField(blank=False)