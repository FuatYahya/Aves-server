from django.core.validators import DecimalValidator
from rest_framework import serializers
from .models import Content
from authentication.models import User


class ContentSerializer(serializers.ModelSerializer):
    '''
    A serializer for content
    '''
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50, min_length=3)
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Content
        fields = ['id', 'name', 'size', 'description',
                  'price', 'key', 'nonce', 'type', 'category', 'owner', 'tag']

    # def validate(self, attrs):
    #     id = attrs.get('id', '')
    #     # todo: add validators for key and nonce after hashing(
    #     print(id)
    #     if not len(id) == 16:
    #         raise TypeError('ID is not supported')
    #     return attrs
