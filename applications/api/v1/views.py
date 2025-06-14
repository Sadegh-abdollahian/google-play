from rest_framework import viewsets
from applications.models import App, Category
from .serializers import AppSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from orders.models import Order


class AppViewset(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = []
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs.get("slug")
        queryset = self.filter_queryset(self.get_queryset())
        app = get_object_or_404(queryset, slug__isexact=slug)
        user = self.request.user

        if app.price == 0 or user.is_superuser:
            return app

        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to access this app.")

        if Order.objects.filter(user=user, app=app, status="purchased").exists():
            return app
        else:
            raise PermissionDenied("You must purchase this app to access it.")


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
