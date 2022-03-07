import re
from CRUDAPP2.forms import PersonForm
from django.core import files
from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render,redirect
from CRUDAPP2.forms import EmployeeForm,StudentForm,PersonForm
from CRUDAPP2.models import EmployeeModel
import datetime
# Create your views here.



def allEmployee(request):
    eobj=EmployeeModel.objects.all()
    #return render(request,'showEmployee.html',{"data":eobj})
    return render(request,'addEmployee.html',{"data":eobj})

def addNewEmp(request):
    eobj=EmployeeForm()
    return render(request,'addEmployee.html',{"form":eobj})

def addEmpdata(request):
    name=request.POST['emp_name']
    epost=request.POST['emp_post']
    econt=request.POST['emp_contact']
    edoj=request.POST['emp_doj']
    #eem=request.POST['emp_email']
    esal=request.POST['emp_salary']
    eobj=EmployeeModel(emp_name=name,emp_post=epost,emp_contact=econt,emp_salary=esal,emp_doj=edoj)
        #eobj=EmployeeModel(eform)
    eobj.save()
    #return redirect('/CRUDAPP2/addEmp')
    return redirect('/CRUDAPP2/showEmp')
'''
    eform=EmployeeForm(request.POST)
    if eform.is_valid():
        eobj=EmployeeModel(emp_name=eform.name,emp_post=eform.epost,emp_contact=eform.econt,emp_salary=eform.esal,emp_doj=eform.edoj)
        #eobj=EmployeeModel(eform)
        eobj.save()
        return redirect('/CRUDAPP2/showEmp')
    else:
        return redirect('/CRUDAPP2/addEmp')'''

def updateEmp(request,id):
    obj=EmployeeModel.objects.get(pk=id)
    return render(request,'updateEmployee.html',{'Emp':obj})
    #return HttpResponse(obj)

def updateEmp2(request):
    eid=request.POST['eid']
    name=request.POST['ename']
    epost=request.POST['epost']
    econt=request.POST['econ']
    edoj=request.POST['edoj']
    #eem=request.POST['emp_email']
    esal=request.POST['esal']
    eobj=EmployeeModel.objects.get(pk=eid)
    #eobj=EmployeeModel(emp_name=name,emp_post=epost,emp_contact=econt,emp_salary=esal,emp_doj=edoj)
    eobj.emp_name=name
    eobj.emp_post=epost
    eobj.emp_contact=econt
    emp_salary=esal
    emp_doj=edoj
    eobj.save()
    return redirect('/CRUDAPP2/showEmp')

def deleteEmp(request,iid):
    obj=EmployeeModel.objects.get(pk=iid)
    obj.delete()
    return redirect('/CRUDAPP2/showEmp')
   # return HttpResponse(obj)
    #return HttpResponse("FORM EMPLOYEE ADDED")



    #print(name,epost,econt,edoj,eem,esal)






         


