# from backend.accounts.models import User
from django import forms

from backend.utils.utils import has_group

from .models import Call, Category, Subcategory


class CallForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoria',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Call
        fields = (
            'title',
            'description',
            'status',
            'user',
            'category',
            'subcategory',
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        if has_group(self.request.user, 'Padrão'):
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['status'].widget.attrs['hidden'] = True

        if has_group(self.request.user, 'Suporte'):
            for field_name, field in self.fields.items():
                if field_name != 'user':
                    field.widget.attrs['readonly'] = True

                if field_name in ('status', 'subcategory'):
                    field.widget.attrs['hidden'] = True

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('user'):
            self.cleaned_data['user'] = self.request.user

        return self.cleaned_data


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = '__all__'
