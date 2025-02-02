from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Jobs, Company
from .serializers import JobSerializer, CompanySerializer
# Create your views here.


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
