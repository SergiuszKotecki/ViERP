from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CustomerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Customer class"""

    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderProduct class"""

    queryset = models.OrderProduct.objects.all()
    serializer_class = serializers.OrderProductSerializer
    permission_classes = [permissions.IsAuthenticated]
