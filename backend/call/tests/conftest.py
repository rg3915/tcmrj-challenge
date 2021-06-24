import pytest

from backend.accounts.models import User
from backend.call.models import Category, Subcategory


@pytest.fixture
def user():
    data = {
        "first_name": "Regis",
        "last_name": "Santos",
        "email": "regis@email.com"
    }
    user = User.objects.create(**data)
    return user


@pytest.fixture
def category():
    data = {
        "title": "Ar-condicionado"
    }
    category = Category.objects.create(**data)
    return category


@pytest.fixture
def subcategory(category):
    data = {
        "title": "Split",
        "category_id": category.id
    }
    subcategory = Subcategory.objects.create(**data)
    return subcategory


@pytest.fixture
def call(user, subcategory):
    data = {
        "title": "Lorem",
        "description": "lorem ipsum dollor",
        "status": "a",
        "user_id": user.id,
        "subcategory_id": subcategory.id
    }
    return data
