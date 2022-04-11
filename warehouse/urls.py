from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Seller", api.SellerViewSet)
router.register("ProductBatch", api.ProductBatchViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("warehouse/Seller/", views.SellerListView.as_view(), name="warehouse_Seller_list"),
    path("warehouse/Seller/create/", views.SellerCreateView.as_view(), name="warehouse_Seller_create"),
    path("warehouse/Seller/detail/<slug:slug>/", views.SellerDetailView.as_view(), name="warehouse_Seller_detail"),
    path("warehouse/Seller/update/<slug:slug>/", views.SellerUpdateView.as_view(), name="warehouse_Seller_update"),
    path("warehouse/Seller/delete/<slug:slug>/", views.SellerDeleteView.as_view(), name="warehouse_Seller_delete"),
    path("warehouse/ProductBatch/", views.ProductBatchListView.as_view(), name="warehouse_ProductBatch_list"),
    path("warehouse/ProductBatch/create/", views.ProductBatchCreateView.as_view(), name="warehouse_ProductBatch_create"),
    path("warehouse/ProductBatch/detail/<int:pk>/", views.ProductBatchDetailView.as_view(), name="warehouse_ProductBatch_detail"),
    path("warehouse/ProductBatch/update/<int:pk>/", views.ProductBatchUpdateView.as_view(), name="warehouse_ProductBatch_update"),
    path("warehouse/ProductBatch/delete/<int:pk>/", views.ProductBatchDeleteView.as_view(), name="warehouse_ProductBatch_delete"),
)
