from django import forms
from CRUDAPP2.models import PersonModel

class EmployeeForm(forms.Form):
    emp_name=forms.CharField(max_length=25)
    emp_post=forms.CharField(max_length=20)
    emp_contact=forms.IntegerField()
    emp_salary=forms.IntegerField()
    emp_doj=forms.DateField()
    #emp_email=forms.EmailField()

class StudentForm(forms.Form):
    name=forms.CharField(max_length=25)
    file=forms.FileField()


class PersonForm(forms.ModelForm):
    class Meta:
        model=PersonModel
        fields="__all__"