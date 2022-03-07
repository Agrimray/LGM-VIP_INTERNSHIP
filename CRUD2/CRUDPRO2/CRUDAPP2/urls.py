from django.contrib import admin
from django.urls import path
from CRUDAPP2 import views

urlpatterns = [
    path('showEmp',views.allEmployee),
    path('addEmp',views.addNewEmp),
    path('addEmpdata',views.addEmpdata),
    path('deleteEmp/<int:iid>',views.deleteEmp),
    path('updateEmp/<int:id>',views.updateEmp),
    path('updateEmp2',views.updateEmp2),
    
]