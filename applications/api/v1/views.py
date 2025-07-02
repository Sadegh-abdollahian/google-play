from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from applications.models import App, Category
from orders.models import Order
from .serializers import AppSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
from django.db.models import F


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


def download_app(request, app_slug):
    """
    This view increments the download count of an app and serves the APK file.
    """

    app = get_object_or_404(App, slug=app_slug)
    user = request.user

    if (
        app.price != 0
        and not Order.objects.filter(user=user, app=app, status="purchased").exists()
    ):
        return HttpResponse("Payment is required to access this app.", status=402)

    # Increment the download count atomically
    App.objects.filter(pk=app.pk).update(downloads=F("downloads") + 1)

    # Serve the file
    return FileResponse(app.apk_file.open(), as_attachment=True)
