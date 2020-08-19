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
    #all_users = list(all_users)
    pricelist=PricingPlanOption.objects.all() 
    #print("pricelistttttttttttt",pricelist)
    price_list=[]
    # for price in pricelist:
    #     price_list.append(price.price)
    # price_list_dict={'price_list':price_list}
    # all_users.append(price_list_dict)    
    # print(price_list)     
    context={'all_users':all_users,'price_list':price_list}
    return render(request,'priceapp/index.html',context)        
    #return render(request,'/src/index.html')
# class PricingPlanList(APIView):
#     def get(self,request):
#         PricingPlan_obj=PricingPlan.objects.all()
#         serializer=PricingPlanSerializer(PricingPlan_obj,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PricingPlanSerializer(data=request.data,context={"request": request.data})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PricingPlanOptionList(APIView):
#     def get(self,request):
#         PricingPlanOption_obj=PricingPlanOption.objects.all()
#         serializer=PricingPlanOptionSerializer(PricingPlanOption_obj,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         pass     

# class PricingDelhiList(APIView):
#     def get(self,request):
#         obj_one=PricingPlan.objects.all()
#         serializer=PricingDelhiSerializer(obj_one,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         pass     

# class PricingHyderabadList(APIView):
#     def get(self,request):
#         obj_one=PricingPlanOption.objects.all()
#         serializer=PricingHyderabadSerializer(obj_one,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         pass     


def create(request):
    if request.method == 'POST':
        form = PricingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PricingPlanForm()

    return render(request,'priceapp/create.html',{'form': form})

def edit(request, pk, template_name='priceapp/edit.html'):
    contact = get_object_or_404(PricingPlan, pk=pk)
    form = PricingPlanForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='priceapp/confirm_delete.html'):
    contact = get_object_or_404(PricingPlan, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})

