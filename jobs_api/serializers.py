
from rest_framework import serializers
from .models import Jobs, Company

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Jobs
        fields= "__all__"
        
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Company
        fields= "__all__"