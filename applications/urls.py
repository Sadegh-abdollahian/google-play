from django.urls import path, include

app_name = "applications"

urlpatterns = [
    path("api/v1/", include("applications.api.v1.urls")),
]
