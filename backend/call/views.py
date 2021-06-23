from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from backend.core.mixins import ObjectModel, TotalItems

from .forms import CallForm, CategoryForm
from .mixins import SearchCallMixin
from .models import Call, Category


class CallListView(LRM, TotalItems, SearchCallMixin, ListView):
    model = Call
    paginate_by = 20


class CallCreateView(LRM, ObjectModel, CreateView):
    model = Call
    form_class = CallForm


class CallDetailView(LRM, DetailView):
    model = Call


class CallUpdateView(LRM, UpdateView):
    model = Call
    form_class = CallForm


class CategoryListView(LRM, TotalItems, SearchCallMixin, ListView):
    model = Category
    paginate_by = 20


class CategoryDetailView(LRM, DetailView):
    model = Category


class CategoryCreateView(LRM, ObjectModel, CreateView):
    model = Category
    form_class = CategoryForm


class CategoryUpdateView(LRM, UpdateView):
    model = Category
    form_class = CategoryForm


class CategoryDeleteView(LRM, DeleteView):
    model = Category
    success_url = reverse_lazy('call:category_list')
