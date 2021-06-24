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
            'created_by',
            'user',
            'category',
            'subcategory',
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        if has_group(self.request.user, 'Padrão'):
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['created_by'].widget = forms.HiddenInput()
            self.fields['status'].widget.attrs['hidden'] = True

        if has_group(self.request.user, 'Suporte'):
            for field_name, field in self.fields.items():
                if field_name in ('title', 'description'):
                    field.widget.attrs['readonly'] = True

                if field_name in ('status', 'category', 'subcategory', 'created_by'):
                    field.widget.attrs['hidden'] = True

        if has_group(self.request.user, 'Gestor'):
            self.fields['created_by'].widget.attrs['hidden'] = True

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('created_by'):
            self.cleaned_data['created_by'] = self.request.user

        return self.cleaned_data


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = '__all__'
