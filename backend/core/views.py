from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from backend.call.constants import CONCLUDED, IN_PROGRESS, OPEN
from backend.call.models import Call
from backend.utils.utils import has_group


@login_required
def index(request):
    template_name = 'index.html'

    queryset = Call.objects.all()

    if has_group(request.user, 'Padrão'):
        queryset = queryset.filter(user=request.user)

    open_status = queryset.filter(status=OPEN).count()
    in_progress_status = queryset.filter(status=IN_PROGRESS).count()
    concluded_status = queryset.filter(status=CONCLUDED).count()

    context = {
        'open_status': open_status,
        'in_progress_status': in_progress_status,
        'concluded_status': concluded_status,
    }
    return render(request, template_name, context)
