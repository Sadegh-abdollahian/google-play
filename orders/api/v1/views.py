from rest_framework import viewsets, serializers, response, status
from orders.models import Order
from .serializers import OrderSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # Requires payment logic
    def perform_create(self, serializer):
        if Order.objects.filter(
            user=self.request.user, app=serializer.validated_data.get("app")
        ).exists():
            raise PermissionDenied("You have already purchased this app.")

        if serializer.is_valid():
            if (
                serializer.validated_data.get("total_amount")
                != serializer.validated_data.get("app").price
            ):
                raise PermissionDenied("Total amount is not correct.")
            serializer.save(user=self.request.user)

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return serializers.ValidationError("Serializer is not valid.")

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
