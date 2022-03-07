from django.contrib import admin
from CRUDAPP2.models import  PersonModel,EmployeeModel
# Register your models here.
admin.site.register(PersonModel)
admin.site.register(EmployeeModel)