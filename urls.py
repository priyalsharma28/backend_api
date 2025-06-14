from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
