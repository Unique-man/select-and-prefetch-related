from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    LOC=models.CharField(max_length=100)
    def __str__(self):
        return str(self.DEPTNO)
    
class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.DecimalField(max_digits=10,decimal_places=2)
    COMM=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.EMPNO)
    

