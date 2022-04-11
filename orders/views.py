from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CustomerListView(generic.ListView):
    model = models.Customer
    form_class = forms.CustomerForm


class CustomerCreateView(generic.CreateView):
    model = models.Customer
    form_class = forms.CustomerForm


class CustomerDetailView(generic.DetailView):
    model = models.Customer
    form_class = forms.CustomerForm


class CustomerUpdateView(generic.UpdateView):
    model = models.Customer
    form_class = forms.CustomerForm
    pk_url_kwarg = "pk"


class CustomerDeleteView(generic.DeleteView):
    model = models.Customer
    success_url = reverse_lazy("orders_Customer_list")


class OrderListView(generic.ListView):
    model = models.Order
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "pk"


class OrderDeleteView(generic.DeleteView):
    model = models.Order
    success_url = reverse_lazy("orders_Order_list")


class OrderProductListView(generic.ListView):
    model = models.OrderProduct
    form_class = forms.OrderProductForm


class OrderProductCreateView(generic.CreateView):
    model = models.OrderProduct
    form_class = forms.OrderProductForm


class OrderProductDetailView(generic.DetailView):
    model = models.OrderProduct
    form_class = forms.OrderProductForm


class OrderProductUpdateView(generic.UpdateView):
    model = models.OrderProduct
    form_class = forms.OrderProductForm
    pk_url_kwarg = "pk"


class OrderProductDeleteView(generic.DeleteView):
    model = models.OrderProduct
    success_url = reverse_lazy("orders_OrderProduct_list")
