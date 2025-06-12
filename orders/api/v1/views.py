from rest_framework import viewsets
from orders.models import Order
from .serializers import OrderSerializer
from rest_framework.exceptions import PermissionDenied


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    def perform_create(self, serializer):
        if Order.objects.filter(
            user=self.request.user, app=serializer.validated_data.get("app")
        ).exists():
            print(
                Order.objects.filter(
                    user=self.request.user, app=serializer.validated_data.get("app")
                )
            )
            raise PermissionDenied("You have already purchased this app.")

        if serializer.is_valid():
            serializer.save(user=self.request.user)
