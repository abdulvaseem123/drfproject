from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PricingPlan,PricingPlanOption
from .serializers import PricingPlanSerializer,PricingPlanOptionSerializer,PricingDelhiSerializer,PricingHyderabadSerializer



class PricingPlanList(APIView):
    def get(self,request):
        PricingPlan_obj=PricingPlan.objects.all()
        serializer=PricingPlanSerializer(PricingPlan_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass 

class PricingPlanOptionList(APIView):
    def get(self,request):
        PricingPlanOption_obj=PricingPlanOption.objects.all()
        serializer=PricingPlanOptionSerializer(PricingPlanOption_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass     

class PricingDelhiList(APIView):
    def get(self,request):
        obj_one=PricingPlan.objects.all()
        serializer=PricingDelhiSerializer(obj_one,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass     

class PricingHyderabadList(APIView):
    def get(self,request):
        obj_one=PricingPlanOption.objects.all()
        serializer=PricingHyderabadSerializer(obj_one,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass     


