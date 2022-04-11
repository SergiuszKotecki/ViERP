from django.db import models
from django.urls import reverse


class Seller(models.Model):

    # Fields
    url = models.URLField()
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    platform = models.CharField(max_length=250)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("warehouse_Seller_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("warehouse_Seller_update", args=(self.slug,))


class ProductBatch(models.Model):

    # Relationships
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    seller = models.ForeignKey("warehouse.Seller", on_delete=models.CASCADE)

    # Fields
    purchase_price_usd = models.FloatField(null=True, blank=True)
    purchase_date = models.DateField(auto_now=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    quantity = models.PositiveIntegerField()
    purchase_price_pln = models.FloatField(null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("warehouse_ProductBatch_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("warehouse_ProductBatch_update", args=(self.pk,))
