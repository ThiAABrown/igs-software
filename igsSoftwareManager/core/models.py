from django.db import models

class Employees(models.Model):
    name = models.CharField('Name', max_length=255)
    email = models.CharField('E-mail', max_length=255)
    department = models.OneToOneField('Departments', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 

class Departments(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name