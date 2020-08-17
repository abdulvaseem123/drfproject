from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.HomePageView.as_view()),
    #path('links/', views.LinksPageView.as_view()),
    
]