from django.urls import path
from .views import SendOTP, RegisterView, LoginView, wishListViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("whishlist", wishListViewset, basename="whishlist")

urlpatterns = [
    path("send_otp/", SendOTP.as_view(), name="send_otp"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
