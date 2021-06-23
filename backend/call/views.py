from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import ListView

from backend.core.mixins import TotalItems

from .models import Call


class CallListView(LRM, TotalItems, ListView):
    model = Call
    paginate_by = 20
