from django.shortcuts import render

from .models import Employees, Departments

def employees(request):
    context = {
        'employees': Employees.objects.all()
    }
    return render(request, 'employees.html', context )