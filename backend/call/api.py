from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from backend.accounts.models import User

from .models import Call, Subcategory

router = Router()

CallSchema = create_schema(Call)


class CallSchemaIn(Schema):
    title: str
    description: str
    status: str = 'a'
    user_id: int
    subcategory_id: int


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
