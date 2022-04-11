from rest_framework import serializers

from . import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = [
            "surname",
            "country",
            "address",
            "name",
            "city",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "order_date",
        ]

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderProduct
        fields = [
            "quantity",
            "quantity",
        ]
