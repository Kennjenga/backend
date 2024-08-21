from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget= forms.TextInput(attrs = {
        "placeholder": "Name of product",
    }))
    description = forms.CharField(required=False, widget= forms.Textarea(attrs={
        "class": "new-class-name two",
        "rows": 10,
        "cols": 40,
    }))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price', 
        ]
    
    def clean_title(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not "ABC" in name:
            raise forms.ValidationError("This is an invalid title")
        raise name
    

class RawProductForm(forms.Form):
    name = forms.CharField(label="Name", widget= forms.TextInput(attrs = {
        "placeholder": "Name of product",
    }))
    description = forms.CharField(required=False, widget= forms.Textarea(attrs={
        "class": "new-class-name two",
        "rows": 10,
        "cols": 40,
    }))
    price = forms.DecimalField(initial=199.99)
