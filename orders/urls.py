from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Customer", api.CustomerViewSet)
router.register("Order", api.OrderViewSet)
router.register("OrderProduct", api.OrderProductViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("orders/Customer/", views.CustomerListView.as_view(), name="orders_Customer_list"),
    path("orders/Customer/create/", views.CustomerCreateView.as_view(), name="orders_Customer_create"),
    path("orders/Customer/detail/<int:pk>/", views.CustomerDetailView.as_view(), name="orders_Customer_detail"),
    path("orders/Customer/update/<int:pk>/", views.CustomerUpdateView.as_view(), name="orders_Customer_update"),
    path("orders/Customer/delete/<int:pk>/", views.CustomerDeleteView.as_view(), name="orders_Customer_delete"),
    path("orders/Order/", views.OrderListView.as_view(), name="orders_Order_list"),
    path("orders/Order/create/", views.OrderCreateView.as_view(), name="orders_Order_create"),
    path("orders/Order/detail/<int:pk>/", views.OrderDetailView.as_view(), name="orders_Order_detail"),
    path("orders/Order/update/<int:pk>/", views.OrderUpdateView.as_view(), name="orders_Order_update"),
    path("orders/Order/delete/<int:pk>/", views.OrderDeleteView.as_view(), name="orders_Order_delete"),
    path("orders/OrderProduct/", views.OrderProductListView.as_view(), name="orders_OrderProduct_list"),
    path("orders/OrderProduct/create/", views.OrderProductCreateView.as_view(), name="orders_OrderProduct_create"),
    path("orders/OrderProduct/detail/<int:pk>/", views.OrderProductDetailView.as_view(), name="orders_OrderProduct_detail"),
    path("orders/OrderProduct/update/<int:pk>/", views.OrderProductUpdateView.as_view(), name="orders_OrderProduct_update"),
    path("orders/OrderProduct/delete/<int:pk>/", views.OrderProductDeleteView.as_view(), name="orders_OrderProduct_delete"),
)
