from posixpath import basename

from django.urls import path, include
from rest_framework import routers

from .views import employees
from core.api.viewsets import EmployeesViewSet, DepartmentsViewSet

route = routers.DefaultRouter()
route.register(r'employees', EmployeesViewSet, basename="Employees")
route.register(r'departments', DepartmentsViewSet, basename="Departments")

urlpatterns = [
    path('', employees, name='employees'),
    path('api/', include(route.urls))
]