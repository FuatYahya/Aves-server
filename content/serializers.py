from django.core.validators import DecimalValidator
from rest_framework import serializers
from rest_framework.fields import ImageField
from .models import Content
from authentication.models import User


class ContentSerializer(serializers.ModelSerializer):
    '''
    A serializer for content
    '''
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50, min_length=3)
    # size = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True)
    is_preview = serializers.BooleanField(read_only=True)
    likes = serializers.IntegerField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)
    file = serializers.FileField(read_only=True)

    class Meta:
        model = Content
        fields = ['id', 'name', 'size', 'description',
                  'price', 'is_preview', 'type', 'category', 'image', 'file', 'likes', 'views', 'owner', 'tags']
