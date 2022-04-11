from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SellerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Seller class"""

    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductBatchViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProductBatch class"""

    queryset = models.ProductBatch.objects.all()
    serializer_class = serializers.ProductBatchSerializer
    permission_classes = [permissions.IsAuthenticated]
