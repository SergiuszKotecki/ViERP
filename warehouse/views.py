from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class SellerListView(generic.ListView):
    model = models.Seller
    form_class = forms.SellerForm


class SellerCreateView(generic.CreateView):
    model = models.Seller
    form_class = forms.SellerForm


class SellerDetailView(generic.DetailView):
    model = models.Seller
    form_class = forms.SellerForm
    slug_url_kwarg = "slug"


class SellerUpdateView(generic.UpdateView):
    model = models.Seller
    form_class = forms.SellerForm
    slug_url_kwarg = "slug"


class SellerDeleteView(generic.DeleteView):
    model = models.Seller
    success_url = reverse_lazy("warehouse_Seller_list")


class ProductBatchListView(generic.ListView):
    model = models.ProductBatch
    form_class = forms.ProductBatchForm


class ProductBatchCreateView(generic.CreateView):
    model = models.ProductBatch
    form_class = forms.ProductBatchForm


class ProductBatchDetailView(generic.DetailView):
    model = models.ProductBatch
    form_class = forms.ProductBatchForm


class ProductBatchUpdateView(generic.UpdateView):
    model = models.ProductBatch
    form_class = forms.ProductBatchForm
    pk_url_kwarg = "pk"


class ProductBatchDeleteView(generic.DeleteView):
    model = models.ProductBatch
    success_url = reverse_lazy("warehouse_ProductBatch_list")
