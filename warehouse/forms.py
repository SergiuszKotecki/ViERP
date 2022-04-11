from django import forms
from . import models


class SellerForm(forms.ModelForm):
    class Meta:
        model = models.Seller
        fields = [
            "url",
            "name",
            "slug",
            "platform",
        ]


class ProductBatchForm(forms.ModelForm):
    class Meta:
        model = models.ProductBatch
        fields = [
            "purchase_price_usd",
            "purchase_date",
            "quantity",
            "purchase_price_pln",
            "product",
            "seller",
        ]
