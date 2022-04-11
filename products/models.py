from django.db import models
from django.urls import reverse


class Product(models.Model):

    # Fields
    name = models.CharField(max_length=250)
    product_image = models.ImageField('/images/products/')
    published = models.DateField()
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("products_Product_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("products_Product_update", args=(self.slug,))
