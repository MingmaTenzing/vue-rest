
from rest_framework import serializers
from .models import Jobs, Company

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Jobs
        fields= [ "id", "url", 'title', 'type', 'location', 'description', 'company' ]
        
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Company
        fields= "__all__"