from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from applications.models import App, Category
from orders.models import Order
from .serializers import AppSerializer, CategorySerializer
from .permissions import IsAppOwnerOrReadOnly
from .filters import AppFilter
from accounts.models import User
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
from django.db.models import F
from django.utils.text import slugify
from faker import Faker
from django_filters.rest_framework import DjangoFilterBackend


class AppViewset(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAppOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppFilter
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(status="drafted")


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    lookup_field = "slug"

    # This action returns every app with the same category
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
        user.is_authenticated
        and app.price != 0
        and not Order.objects.filter(user=user, app=app, status="purchased").exists()
    ):
        return HttpResponse("Payment is required to access this app.", status=402)

    # Increment the download count atomically
    App.objects.filter(pk=app.pk).update(downloads=F("downloads") + 1)

    # Serve the file
    return FileResponse(app.apk_file.open(), as_attachment=True)


def add_fake_data(request):
    """
    This function generates fake data for the App model
    """
    fake = Faker()
    # The number in the range function is the amount of fake data that are
    # going to be generated
    for _ in range(10):
        App.objects.create(
            apk_file=fake.file_extension(category="image"),
            name=fake.name(),
            subname=fake.name(),
            icon_image=fake.file_extension(category="image"),
            status="published",
            category=get_object_or_404(Category, id=1),
            legal_age=fake.random_int(min=3, max=18),
            downloads="0",
            about=fake.text(),
            price=fake.random_int(min=0, max=3_000_000),
            slug=slugify(fake.name()),
            tags="action",
            owner=get_object_or_404(User, id=1),
        )
