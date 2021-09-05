from django.db import models
from django.db.models.fields import CharField
from authentication.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tag


class Content(models.Model):
    CHOICES_TYPE = [
        ('Audio', 'Audio'),
        ('Video', 'Video'),
    ]

    CHOICES_CATEGORY = [
        ('Tutorial', 'Tutorial'),
        ('Movie', 'Movie'),
        ('Music', 'Music'),
        ('Audio Book', 'Audio Book'),
    ]

    id = models.UUIDField(primary_key=True, db_index=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    size = models.BigIntegerField(null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    # todo: change key to hashed
    key = CharField(max_length=16, blank=False, null=False)
    nonce = CharField(max_length=12, blank=False, null=False)
    type = models.CharField(
        max_length=25, choices=CHOICES_TYPE, blank=False, null=False)
    category = models.CharField(
        max_length=25, choices=CHOICES_CATEGORY, blank=False, null=False)
    tag = models.ManyToManyField(to=Tag)
    # image = models.ImageField(blank=False, null=False)
    is_preview = models.BooleanField(default=False)
    owner = models.ForeignKey(
        to=User, on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
