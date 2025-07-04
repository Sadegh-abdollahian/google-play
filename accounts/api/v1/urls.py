from django.urls import path, include
from .views import SendOTP, RegisterView, LoginView, BookMarkView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"bookmarks", BookMarkView, basename="bookmarks")

urlpatterns = [
    path("send_otp/", SendOTP.as_view(), name="send_otp"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
