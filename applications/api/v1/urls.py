from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"apps", views.AppViewset)
router.register(r"categories", views.CategoryViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("download/<slug:app_slug>/", views.download_app, name="download_app"),
    path("add_fake_data/", views.add_fake_data, name="add_fake_data"),
]
