# from backend.accounts.models import User
from django import forms

from backend.utils.utils import has_group

from .models import Call, Category, Subcategory


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        if has_group(self.request.user, 'Padrão'):
            self.fields['user'].widget = forms.HiddenInput()

        if has_group(self.request.user, 'Suporte'):
            for field_name, field in self.fields.items():
                if field_name != 'user':
                    field.widget.attrs['readonly'] = True

                if field_name in ('status', 'subcategory'):
                    field.widget = forms.HiddenInput()

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
