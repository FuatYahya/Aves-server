from django.db import models
from authentication.models import User
from payment.models import Method
from content.models import Content


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    content = models.ForeignKey(to=Content, on_delete=models.DO_NOTHING)
    payment_method = models.ForeignKey(to=Method, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
