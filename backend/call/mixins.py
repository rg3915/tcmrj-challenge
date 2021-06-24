from django.db.models import Q

from backend.utils.utils import has_group


class SearchCallMixin:

    def get_queryset(self):
        queryset = super(SearchCallMixin, self).get_queryset()

        if has_group(self.request.user, 'Padrão'):
            queryset = queryset.filter(user=self.request.user)

        data = self.request.GET
        search = data.get('search')
        status = data.get('status')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) |
                Q(user__email__icontains=search) |
                Q(created_by__first_name__icontains=search) |
                Q(created_by__last_name__icontains=search) |
                Q(created_by__email__icontains=search) |
                Q(description__icontains=search)
            )
        if status:
            queryset = queryset.filter(status=status)

        return queryset


class FormKwargsMixin:

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
