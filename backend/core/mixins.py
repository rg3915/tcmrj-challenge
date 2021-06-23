class ObjectModel:

    def get_context_data(self, **kwargs):
        kwargs['object'] = self.model
        return super().get_context_data(**kwargs)


class TotalItems:

    def get_context_data(self, **kwargs):
        items_total = self.model.objects.values_list('id', flat=True).count()
        kwargs['total_items'] = items_total
        return super().get_context_data(**kwargs)
