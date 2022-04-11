import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Customer_list_view():
    instance1 = test_helpers.create_orders_Customer()
    instance2 = test_helpers.create_orders_Customer()
    client = Client()
    url = reverse("orders_Customer_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Customer_create_view():
    client = Client()
    url = reverse("orders_Customer_create")
    data = {
        "surname": "text",
        "country": "text",
        "address": "text",
        "name": "text",
        "city": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Customer_detail_view():
    client = Client()
    instance = test_helpers.create_orders_Customer()
    url = reverse("orders_Customer_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Customer_update_view():
    client = Client()
    instance = test_helpers.create_orders_Customer()
    url = reverse("orders_Customer_update", args=[instance.pk, ])
    data = {
        "surname": "text",
        "country": "text",
        "address": "text",
        "name": "text",
        "city": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_list_view():
    instance1 = test_helpers.create_orders_Order()
    instance2 = test_helpers.create_orders_Order()
    client = Client()
    url = reverse("orders_Order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_create_view():
    customer = test_helpers.create_orders_Customer()
    client = Client()
    url = reverse("orders_Order_create")
    data = {
        "order_date": datetime.now(),
        "customer": customer.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_detail_view():
    client = Client()
    instance = test_helpers.create_orders_Order()
    url = reverse("orders_Order_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_update_view():
    customer = test_helpers.create_orders_Customer()
    client = Client()
    instance = test_helpers.create_orders_Order()
    url = reverse("orders_Order_update", args=[instance.pk, ])
    data = {
        "order_date": datetime.now(),
        "customer": customer.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderProduct_list_view():
    instance1 = test_helpers.create_orders_OrderProduct()
    instance2 = test_helpers.create_orders_OrderProduct()
    client = Client()
    url = reverse("orders_OrderProduct_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_OrderProduct_create_view():
    product = test_helpers.create_products_Product()
    order = test_helpers.create_orders_Order()
    client = Client()
    url = reverse("orders_OrderProduct_create")
    data = {
        "quantity": 1,
        "quantity": 1,
        "product": product.pk,
        "order": order.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderProduct_detail_view():
    client = Client()
    instance = test_helpers.create_orders_OrderProduct()
    url = reverse("orders_OrderProduct_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_OrderProduct_update_view():
    product = test_helpers.create_products_Product()
    order = test_helpers.create_orders_Order()
    client = Client()
    instance = test_helpers.create_orders_OrderProduct()
    url = reverse("orders_OrderProduct_update", args=[instance.pk, ])
    data = {
        "quantity": 1,
        "quantity": 1,
        "product": product.pk,
        "order": order.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
