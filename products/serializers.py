from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "name",
            "product_image",
            "published",
            "description",
            "slug",
        ]
