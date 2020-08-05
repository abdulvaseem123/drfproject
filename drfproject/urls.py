"""drfproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from priceapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.PricingPlanList)
router.register('apioption',views.PricingPlanOptionList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('dashboard/', include('priceapp.urls')),
    #path('api/', views.PricingPlanList.as_view()),
    # path('priceoption/', views.PricingPlanOptionList.as_view()),
    # path('price/delhi',views.PricingDelhiList.as_view()),
    # path('price/hyderabad',views.PricingHyderabadList.as_view()),
]
