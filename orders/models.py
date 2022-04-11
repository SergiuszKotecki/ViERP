from django.db import models
from django.urls import reverse


class Customer(models.Model):

    # Fields
    surname = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("orders_Customer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("orders_Customer_update", args=(self.pk,))


class Order(models.Model):

    # Relationships
    customer = models.OneToOneField("orders.Customer", on_delete=models.CASCADE)

    # Fields
    order_date = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("orders_Order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("orders_Order_update", args=(self.pk,))


class OrderProduct(models.Model):

    # Relationships
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)

    # Fields
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("orders_OrderProduct_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("orders_OrderProduct_update", args=(self.pk,))
