from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
