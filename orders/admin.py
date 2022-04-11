from django.contrib import admin
from django import forms

from . import models


class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        fields = "__all__"


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = [
        "surname",
        "country",
        "address",
        "name",
        "city",
    ]
    readonly_fields = [
        "surname",
        "country",
        "address",
        "name",
        "city",
    ]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "order_date",
    ]
    readonly_fields = [
        "order_date",
    ]


class OrderProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderProduct
        fields = "__all__"


class OrderProductAdmin(admin.ModelAdmin):
    form = OrderProductAdminForm
    list_display = [
        "quantity",
        "quantity",
    ]
    readonly_fields = [
        "quantity",
        "quantity",
    ]


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderProduct, OrderProductAdmin)
