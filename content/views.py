from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ContentSerializer
from helpers.utils import Util
from .models import Content
from .permissions import IsOwner


class CreateContentApiView(generics.CreateAPIView):
    '''
    Api endpoint to create contents
    '''
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        return serializer.save(id=Util.create_uuid(), owner=self.request.user)

    def get_queryset(self):
        self.permission_classes = ()
        return self.queryset.filter()


class ContentsApiView(generics.ListAPIView):
    '''
    Api endpoint to get contents
    '''
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_queryset(self):
        self.permission_classes = ()
        return self.queryset.filter()


class GetContentApiView(generics.RetrieveAPIView):
    '''
    Api endpoint to fet contents using content uuid
    '''
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter()


class EditContentApiView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Api endpoint to edit contents using owner(user) and perform update, delete
    '''
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(id=Util.create_uuid(), owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter()
