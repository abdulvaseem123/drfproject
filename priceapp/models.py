from django.db import models
from django.urls import reverse

class PricingPlan(models.Model):
    planname=models.CharField(max_length=45)
    description=models.CharField(max_length=45)
    planformula=models.CharField(max_length=45)
    location=models.CharField(max_length=45)
    planstatus=models.CharField(max_length=1)
    createdate=models.DateField(auto_now=True)
    updatedate=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.planname

class PricingPlanOption(models.Model):
    planid=models.CharField(max_length=45)
    price=models.DecimalField(decimal_places=3,max_digits=10)
    status=models.CharField(max_length=1)
    createdate=models.DateField(auto_now=True)
    updatedate=models.DateField(auto_now=True) 

    def __str__(self):
        return self.planid   


