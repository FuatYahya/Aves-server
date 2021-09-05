from django.urls import path
from .views import *


urlpatterns = [
    path('', ContentsApiView.as_view(), name="contents"),
    path('create/', CreateContentApiView.as_view(), name="craete-content"),
    path('get/<str:id>', GetContentApiView.as_view(), name="get-content"),
    path('edit/<str:id>', EditContentApiView.as_view(), name="edit-content"),
]
