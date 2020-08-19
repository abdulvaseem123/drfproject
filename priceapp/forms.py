from django import forms
from .models import PricingPlan

class PricingPlanForm(forms.ModelForm):
    class Meta:
        model = PricingPlan
        fields = "__all__"