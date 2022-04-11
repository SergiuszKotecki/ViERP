from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm
    slug_url_kwarg = "slug"


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    slug_url_kwarg = "slug"


class ProductDeleteView(generic.DeleteView):
    model = models.Product
    success_url = reverse_lazy("products_Product_list")
