import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Seller_list_view():
    instance1 = test_helpers.create_warehouse_Seller()
    instance2 = test_helpers.create_warehouse_Seller()
    client = Client()
    url = reverse("warehouse_Seller_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Seller_create_view():
    client = Client()
    url = reverse("warehouse_Seller_create")
    data = {
        "url": http://127.0.0.1,
        "name": "text",
        "slug": "slug",
        "platform": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Seller_detail_view():
    client = Client()
    instance = test_helpers.create_warehouse_Seller()
    url = reverse("warehouse_Seller_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Seller_update_view():
    client = Client()
    instance = test_helpers.create_warehouse_Seller()
    url = reverse("warehouse_Seller_update", args=[instance.slug, ])
    data = {
        "url": http://127.0.0.1,
        "name": "text",
        "slug": "slug",
        "platform": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ProductBatch_list_view():
    instance1 = test_helpers.create_warehouse_ProductBatch()
    instance2 = test_helpers.create_warehouse_ProductBatch()
    client = Client()
    url = reverse("warehouse_ProductBatch_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ProductBatch_create_view():
    product = test_helpers.create_products_Product()
    seller = test_helpers.create_warehouse_Seller()
    client = Client()
    url = reverse("warehouse_ProductBatch_create")
    data = {
        "purchase_price_usd": 1.0f,
        "purchase_date": datetime.now(),
        "quantity": 1,
        "purchase_price_pln": 1.0f,
        "product": product.pk,
        "seller": seller.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ProductBatch_detail_view():
    client = Client()
    instance = test_helpers.create_warehouse_ProductBatch()
    url = reverse("warehouse_ProductBatch_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ProductBatch_update_view():
    product = test_helpers.create_products_Product()
    seller = test_helpers.create_warehouse_Seller()
    client = Client()
    instance = test_helpers.create_warehouse_ProductBatch()
    url = reverse("warehouse_ProductBatch_update", args=[instance.pk, ])
    data = {
        "purchase_price_usd": 1.0f,
        "purchase_date": datetime.now(),
        "quantity": 1,
        "purchase_price_pln": 1.0f,
        "product": product.pk,
        "seller": seller.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
