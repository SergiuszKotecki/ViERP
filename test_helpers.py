import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from products import models as products_models
from warehouse import models as warehouse_models
from orders import models as orders_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_products_Product(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["product_image"] = ""
    defaults["published"] = datetime.now()
    defaults["description"] = ""
    defaults["slug"] = ""
    defaults.update(**kwargs)
    return products_models.Product.objects.create(**defaults)
def create_warehouse_Seller(**kwargs):
    defaults = {}
    defaults["url"] = ""
    defaults["name"] = ""
    defaults["slug"] = ""
    defaults["platform"] = ""
    defaults.update(**kwargs)
    return warehouse_models.Seller.objects.create(**defaults)
def create_warehouse_ProductBatch(**kwargs):
    defaults = {}
    defaults["purchase_price_usd"] = ""
    defaults["purchase_date"] = datetime.now()
    defaults["quantity"] = ""
    defaults["purchase_price_pln"] = ""
    if "product" not in kwargs:
        defaults["product"] = create_products_Product()
    if "seller" not in kwargs:
        defaults["seller"] = create_warehouse_Seller()
    defaults.update(**kwargs)
    return warehouse_models.ProductBatch.objects.create(**defaults)
def create_orders_Customer(**kwargs):
    defaults = {}
    defaults["surname"] = ""
    defaults["country"] = ""
    defaults["address"] = ""
    defaults["name"] = ""
    defaults["city"] = ""
    defaults.update(**kwargs)
    return orders_models.Customer.objects.create(**defaults)
def create_orders_Order(**kwargs):
    defaults = {}
    defaults["order_date"] = datetime.now()
    if "customer" not in kwargs:
        defaults["customer"] = create_orders_Customer()
    defaults.update(**kwargs)
    return orders_models.Order.objects.create(**defaults)
def create_orders_OrderProduct(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    defaults["quantity"] = ""
    if "product" not in kwargs:
        defaults["product"] = create_products_Product()
    if "order" not in kwargs:
        defaults["order"] = create_orders_Order()
    defaults.update(**kwargs)
    return orders_models.OrderProduct.objects.create(**defaults)
