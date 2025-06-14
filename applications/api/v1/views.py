from rest_framework import viewsets
from applications.models import App, Category
from .serializers import AppSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser


class AppViewset(viewsets.ReadOnlyModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = []
    lookup_field = "slug"


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
