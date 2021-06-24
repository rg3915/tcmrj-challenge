from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from .models import Call

router = Router()

CallSchema = create_schema(Call)


@router.get("/calls", response=List[CallSchema])
def list_calls(request):
    qs = Call.objects.all()
    return qs


@router.get("/calls/{id}", response=CallSchema)
def get_call(request, id: int):
    call = get_object_or_404(Call, id=id)
    return call
