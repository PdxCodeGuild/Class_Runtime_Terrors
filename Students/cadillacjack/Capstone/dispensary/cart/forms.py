from django import forms
from online_shop.models import Product


# product_inventory = Product.objects.get()

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):

    quantity = forms.TypedChoiceField(
        choices = PRODUCT_QUANTITY_CHOICES,
        coerce = int
    )

    override = forms.BooleanField(
        required = False,
        initial = False,
        widget = forms.HiddenInput
    )

