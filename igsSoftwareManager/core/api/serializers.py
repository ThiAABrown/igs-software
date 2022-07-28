from rest_framework import serializers

from core import models

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = '__all__'

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = '__all__'