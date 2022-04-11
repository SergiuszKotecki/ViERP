from django import forms
from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "name",
            "product_image",
            "published",
            "description",
            "slug",
        ]
