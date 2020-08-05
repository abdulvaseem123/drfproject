from django.shortcuts import render

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


