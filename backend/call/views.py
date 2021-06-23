from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from backend.core.mixins import ObjectModel, TotalItems

from .forms import CallForm
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
