from django.db.models import Q


class SearchCallMixin:

    def get_queryset(self):
        queryset = super(SearchCallMixin, self).get_queryset()

        data = self.request.GET
        search = data.get('search')
        status = data.get('status')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        if status:
            queryset = queryset.filter(status=status)

        return queryset
