from rest_framework import serializers

from . import models


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Seller
        fields = [
            "url",
            "name",
            "slug",
            "platform",
        ]

class ProductBatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductBatch
        fields = [
            "purchase_price_usd",
            "purchase_date",
            "last_updated",
            "created",
            "quantity",
            "purchase_price_pln",
        ]
