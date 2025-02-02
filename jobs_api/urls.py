from rest_framework import routers
from django.urls import  include,path
from .views import JobsViewSet, CompanyViewSet

router = routers.DefaultRouter()

router.register(r'jobs', JobsViewSet )
router.register(r'companies', CompanyViewSet)


urlpatterns = [
    path("api/", include(router.urls ))
]

