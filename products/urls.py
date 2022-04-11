from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Product", api.ProductViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("products/Product/", views.ProductListView.as_view(), name="products_Product_list"),
    path("products/Product/create/", views.ProductCreateView.as_view(), name="products_Product_create"),
    path("products/Product/detail/<slug:slug>/", views.ProductDetailView.as_view(), name="products_Product_detail"),
    path("products/Product/update/<slug:slug>/", views.ProductUpdateView.as_view(), name="products_Product_update"),
    path("products/Product/delete/<slug:slug>/", views.ProductDeleteView.as_view(), name="products_Product_delete"),
)
