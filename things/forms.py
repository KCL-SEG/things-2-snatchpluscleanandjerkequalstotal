"""Forms of the project."""

# Create your forms here.

from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
