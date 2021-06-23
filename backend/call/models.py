from django.db import models
from django.urls import reverse_lazy

from backend.core.models import TimeStampedModel

from .constants import STATUS


class Category(TimeStampedModel):
    title = models.CharField('título', max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.title


class Subcategory(TimeStampedModel):
    title = models.CharField('título', max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='categoria',
        related_name='subcategories',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'

    def __str__(self):
        return self.title


class Call(TimeStampedModel):
    title = models.CharField('título', max_length=100, unique=True)
    description = models.TextField('descrição')
    status = models.CharField('status', max_length=1, choices=STATUS, default='a')  # noqa E501

    class Meta:
        ordering = ('title',)
        verbose_name = 'chamado'
        verbose_name_plural = 'chamados'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('call:call_detail', kwargs={'pk': self.pk})

    @property
    def get_list_url(self):
        return reverse_lazy('call:call_list')

    @property
    def get_update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('call:call_update', kwargs=kw)
        return None

    def get_verbose_name(self):
        return self._meta.verbose_name.title()

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural.title()
