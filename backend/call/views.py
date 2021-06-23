from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import ListView, UpdateView

from backend.core.mixins import TotalItems

from .forms import CallForm
from .mixins import SearchCallMixin
from .models import Call


class CallListView(LRM, TotalItems, SearchCallMixin, ListView):
    model = Call
    paginate_by = 20


class CallUpdateView(LRM, UpdateView):
    model = Call
    form_class = CallForm
