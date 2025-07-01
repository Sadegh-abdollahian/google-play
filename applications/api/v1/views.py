from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from applications.models import App, Category
from .serializers import AppSerializer, CategorySerializer


class AppViewset(viewsets.ReadOnlyModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = []
    lookup_field = "slug"


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    lookup_field = "slug"

    @action(detail=True, methods=["get"])
    def apps(self, request, slug=None):
        category = self.get_object()
        apps = category.apps.all()
        serializer = AppSerializer(apps, many=True, context={"request": request})
        return Response(serializer.data)
