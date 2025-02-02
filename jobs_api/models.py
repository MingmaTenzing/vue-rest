from django.db import models

# Create your models here.
class Company(models.Model): 
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    contactEmail = models.CharField(max_length=250)
    contactPhone = models.CharField(max_length=250) 
    
    
class Jobs(models.Model): 
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="Jobs")
    
    

