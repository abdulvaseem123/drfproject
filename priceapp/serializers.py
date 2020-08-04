from rest_framework import serializers
from .models import PricingPlan,PricingPlanOption

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=PricingPlan
        fields='__all__'

class PricingPlanOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=PricingPlanOption
        fields='__all__'

class PricingDelhiSerializer(serializers.ModelSerializer):
    class Meta:
        model=PricingPlan
        fields=('location','planname')

class PricingHyderabadSerializer(serializers.ModelSerializer):
    class Meta:
        model=PricingPlanOption
        fields=('price',)        

