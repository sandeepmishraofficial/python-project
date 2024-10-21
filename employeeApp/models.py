from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username  # corrected __str__ method


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100)
    schoolclgpg = models.CharField(max_length=200, null=True)
    yearofpassingpg = models.CharField(max_length=28, null=True)
    percentagepg = models.CharField(max_length=30, null=True)
    coursegra = models.CharField(max_length=100)
    schoolclggra = models.CharField(max_length=200, null=True)
    yearofpassinggra = models.CharField(max_length=28, null=True)
    percentagegra = models.CharField(max_length=30, null=True)
    coursessc = models.CharField(max_length=100)
    schoolclgssc = models.CharField(max_length=200, null=True)
    yearofpassingssc = models.CharField(max_length=28, null=True)
    percentagessc = models.CharField(max_length=30, null=True)
    coursehsc = models.CharField(max_length=100, null=True)
    schoolclgsc = models.CharField(max_length=200, null=True)
    yearofpassingsc = models.CharField(max_length=28, null=True)
    percentagesc = models.CharField(max_length=30, null=True)
    # gender = models.CharField(max_length=50, null=True)
    # joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username  

# employee Experience

class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100)
    company1desig = models.CharField(max_length=100, null=True)
    company1salary = models.CharField(max_length=100, null=True)
    company1duration = models.CharField(max_length=100, null=True)
    company2name = models.CharField(max_length=100)
    company2desig = models.CharField(max_length=100, null=True)
    company2salary = models.CharField(max_length=100, null=True)
    company2duration = models.CharField(max_length=100, null=True)
    company3name = models.CharField(max_length=100)
    company3desig = models.CharField(max_length=100, null=True)
    company3salary = models.CharField(max_length=100, null=True)
    company3duration = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.user.username  
