from django import forms

from .models import Call, Category, Subcategory


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = '__all__'
