from django import forms
from .models import Brand, Product
from django.core.exceptions import ValidationError


class AddBrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Product.objects.filter(title=title).exists():
            raise ValidationError('This product title already exists.')
        return title


class BrandFilterForm(forms.Form):
    brand = forms.ChoiceField(choices=[(brand.id, brand.title) for brand in Brand.objects.all()])
