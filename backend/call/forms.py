from django import forms

from .models import Call, Category


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
