# from backend.accounts.models import User
from django import forms

from .models import Call, Category, Subcategory


def has_group(user, group_name):
    ''' Verifica se este usuário pertence a um grupo. '''
    if user:
        groups = user.groups.all().values_list('name', flat=True)
        return True if group_name in groups else False
    return False


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        if has_group(self.request.user, 'Padrão'):
            self.fields['user'].widget = forms.HiddenInput()

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
