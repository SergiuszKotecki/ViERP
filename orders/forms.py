from django import forms
from . import models


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = [
            "surname",
            "country",
            "address",
            "name",
            "city",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "order_date",
            "customer",
        ]


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = models.OrderProduct
        fields = [
            "quantity",
            "quantity",
            "product",
            "order",
        ]
