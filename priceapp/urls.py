from django.urls import path

from . import views 
from .views import PricingPlanCreateView,PricingPlanUpdateView,PricingPlanDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', PricingPlanCreateView.as_view(), name='create_form'),
    path('<int:pk>/update/', PricingPlanUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PricingPlanDeleteView.as_view(), name='delete'),
    #path('', views.HomePageView.as_view()),
    #path('links/', views.LinksPageView.as_view()),
    
]