from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from backend.accounts.models import User

from .models import Call, Category, Subcategory

router = Router()

CallSchema = create_schema(Call)
CategorySchema = create_schema(Category)


class CallSchemaIn(Schema):
    title: str
    description: str
    status: str = 'a'
    user_id: int
    subcategory_id: int


class CategorySchemaIn(Schema):
    title: str


@router.get("/calls", response=List[CallSchema])
def list_calls(request):
    qs = Call.objects.all()
    return qs


@router.get("/calls/{id}", response=CallSchema)
def get_call(request, id: int):
    call = get_object_or_404(Call, id=id)
    return call


@router.post("/calls", response=CallSchema)
def create_call(request, payload: CallSchemaIn):
    # Get params
    title = payload.title
    description = payload.description
    status = payload.status
    user_id = payload.user_id
    subcategory_id = payload.subcategory_id

    # Instance models
    # Get user
    user = get_object_or_404(User, id=user_id)

    # Get subcategory
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)

    # Mount dict data
    data = dict(
        title=title,
        description=description,
        status=status,
        user=user,
        subcategory=subcategory,
    )

    # Save data
    call = Call.objects.create(**data)

    return call


@router.put("/calls/{id}", response=CallSchema)
def update_call(request, id: int, payload: CallSchemaIn):
    call = get_object_or_404(Call, id=id)
    for attr, value in payload.dict().items():
        setattr(call, attr, value)
    call.save()
    return call


@router.delete("/calls/{id}")
def delete_call(request, id: int):
    call = get_object_or_404(Call, id=id)
    call.delete()
    return {"success": True}


@router.get("/categories", response=List[CategorySchema])
def list_categories(request):
    qs = Category.objects.all()
    return qs


@router.get("/categories/{id}", response=CategorySchema)
def get_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    return category


@router.post("/categories", response=CategorySchema)
def create_category(request, payload: CategorySchemaIn):
    category = Category.objects.create(**payload.dict())
    return category


@router.put("/categories/{id}", response=CategorySchema)
def update_category(request, id: int, payload: CategorySchemaIn):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return category


@router.delete("/categories/{id}")
def delete_category(request, id: int):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return {"success": True}
