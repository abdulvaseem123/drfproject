from django.shortcuts import render, redirect, get_object_or_404
from .forms import PricingPlanForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PricingPlan,PricingPlanOption
from .serializers import PricingPlanSerializer,PricingPlanOptionSerializer

class PricingPlanList(ModelViewSet):
    queryset=PricingPlan.objects.all()
    serializer_class=PricingPlanSerializer

class PricingPlanOptionList(ModelViewSet):
    queryset=PricingPlanOption.objects.all()
    serializer_class=PricingPlanOptionSerializer

class PricingPlanCreateView(CreateView):
    model = PricingPlan
    fields='__all__'

class PricingPlanUpdateView(UpdateView):
    model = PricingPlan
    fields='__all__'
    

class PricingPlanDeleteView(DeleteView):
    model = PricingPlan
    success_url = '/dashboard'       
        

def index(request):
    all_users=PricingPlan.objects.all()
    pricelist=PricingPlanOption.objects.all() 
    price_list=[]
    context={'all_users':all_users,'price_list':price_list}
    return render(request,'priceapp/index.html',context)        
   



