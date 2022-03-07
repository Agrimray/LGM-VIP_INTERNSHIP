from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_post=models.CharField(max_length=20)
    emp_contact=models.IntegerField()
    emp_salary=models.IntegerField()
    emp_doj=models.DateField()
    #emp_email=models.EmailField()

    def __str__(self):
        return self.emp_name+self.emp_post+str(self.emp_contact)+str(self.emp_doj)+str(self.emp_salary)


    class Meta:
        db_table="employee"

class PersonModel(models.Model):
    pname=models.CharField(max_length=30)
    pcontact=models.IntegerField()

    def __str__(self):
        return self.pname+str(self.pcontact)


    class Meta:
        db_table="tblperson"

