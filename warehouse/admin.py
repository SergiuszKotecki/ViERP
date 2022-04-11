from django.contrib import admin
from django import forms

from . import models


class SellerAdminForm(forms.ModelForm):

    class Meta:
        model = models.Seller
        fields = "__all__"


class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = [
        "url",
        "name",
        "slug",
        "platform",
    ]
    readonly_fields = [
        "url",
        "name",
        "slug",
        "platform",
    ]


class ProductBatchAdminForm(forms.ModelForm):

    class Meta:
        model = models.ProductBatch
        fields = "__all__"


class ProductBatchAdmin(admin.ModelAdmin):
    form = ProductBatchAdminForm
    list_display = [
        "purchase_price_usd",
        "purchase_date",
        "last_updated",
        "created",
        "quantity",
        "purchase_price_pln",
    ]
    readonly_fields = [
        "purchase_price_usd",
        "purchase_date",
        "last_updated",
        "created",
        "quantity",
        "purchase_price_pln",
    ]


admin.site.register(models.Seller, SellerAdmin)
admin.site.register(models.ProductBatch, ProductBatchAdmin)
