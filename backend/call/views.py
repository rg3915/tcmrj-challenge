from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from backend.core.mixins import ObjectModel, TotalItems

from .forms import CallForm, CategoryForm, SubcategoryForm
from .mixins import SearchCallMixin
from .models import Call, Category, Subcategory


class CallListView(LRM, TotalItems, SearchCallMixin, ListView):
    model = Call
    paginate_by = 20


class CallCreateView(LRM, ObjectModel, CreateView):
    model = Call
    form_class = CallForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


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


class SubcategoryListView(LRM, TotalItems, SearchCallMixin, ListView):
    model = Subcategory
    paginate_by = 20


class SubcategoryDetailView(LRM, DetailView):
    model = Subcategory


class SubcategoryCreateView(LRM, ObjectModel, CreateView):
    model = Subcategory
    form_class = SubcategoryForm


class SubcategoryUpdateView(LRM, UpdateView):
    model = Subcategory
    form_class = SubcategoryForm


class SubcategoryDeleteView(LRM, DeleteView):
    model = Subcategory
    success_url = reverse_lazy('call:subcategory_list')


def call_management(request):
    template_name = 'call/management.html'
    return render(request, template_name)
