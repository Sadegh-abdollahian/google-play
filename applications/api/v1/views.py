from rest_framework import viewsets
from applications.models import App, Category
from .serializers import AppSerializer, CategorySerializer


class AppViewset(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = []


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
