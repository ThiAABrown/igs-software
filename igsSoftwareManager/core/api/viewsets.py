from rest_framework import viewsets

from core.api import serializers
from core import models

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeesSerializer
    queryset = models.Employees.objects.all()

class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DepartmentsSerializer
    queryset = models.Departments.objects.all()