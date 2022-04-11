import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Product_list_view():
    instance1 = test_helpers.create_products_Product()
    instance2 = test_helpers.create_products_Product()
    client = Client()
    url = reverse("products_Product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_create_view():
    client = Client()
    url = reverse("products_Product_create")
    data = {
        "name": "text",
        "product_image": "anImage",
        "published": datetime.now(),
        "description": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_detail_view():
    client = Client()
    instance = test_helpers.create_products_Product()
    url = reverse("products_Product_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_update_view():
    client = Client()
    instance = test_helpers.create_products_Product()
    url = reverse("products_Product_update", args=[instance.slug, ])
    data = {
        "name": "text",
        "product_image": "anImage",
        "published": datetime.now(),
        "description": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302
