from django.contrib import admin
from django import forms

from . import models


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "name",
        "product_image",
        "published",
        "description",
        "slug",
    ]
    readonly_fields = [
        "name",
        "product_image",
        "published",
        "description",
        "slug",
    ]


admin.site.register(models.Product, ProductAdmin)
