
from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def insert_dept(request):
    dept=input('enter the deptno: ')
    dn=input('enter the dname: ')
    loc=input('enter the loc: ')
    LDO=Dept.objects.get_or_create(DEPTNO=dept,DNAME=dn,LOC=loc)
    if LDO[1]:
        LDO=Dept.objects.all()
        d={'LDO':LDO}
        return render(request,'display_Dept.html',d)
    else:
        return HttpResponse('Dept is already exist')
    
def insert_emp(request):
    em=int(input('enter the empno: '))
    ena=input('enter the ename: ')
    j=input('enter the job: ')
    mg=input('enter the mgr: ')
    if mg:
        MGO=Emp.objects.filter(EMPNO=int(mg))[0]
    else:
        MGO=None
    Hire=input('enter the hiredate(YYYY-MM-DD):')
    sal=float(input('enter the sal: '))
    co=input('enter the comm: ')
    if co:
        COM=float(co)
    else:
        COM=None  
    dept=int(input('enter the deptno : '))
    DEP=Dept.objects.get(DEPTNO=dept)
    QLEO=Emp.objects.get_or_create(EMPNO=em,ENAME=ena,JOB=j,MGR=MGO, HIREDATE=Hire,SAL=sal,COMM=COM,DEPTNO=DEP)
    if QLEO[1]:
        QLEO=Emp.objects.all()
        d={'QLEO':QLEO}
        return render (request,'display_Emp.html',d)
    else:
        return HttpResponse('emp is already exist')

def display_Emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.order_by("ENAME") #ascending order
    QLEO=Emp.objects.order_by("-ENAME") #descending order
    QLEO=Emp.objects.order_by(Length("ENAME"))  # orders in Ascending order
    QLEO=Emp.objects.order_by(Length("ENAME").desc()) # orders in Descending order
    QLEO=Emp.objects.exclude(DEPTNO=20)  # exclude()
    QLEO=Emp.objects.filter(DEPTNO=30,SAL__gt='1500') # by default comma act as AND operter in ORM
    QLEO=Emp.objects.filter(Q(ENAME__startswith='A') | Q(DEPTNO=30))
    d={'QLEO':QLEO}
    return render (request,'display_Emp.html',d)

def display_Dept(request):
    LDO=Dept.objects.all()
    d={'LDO':LDO}
    return render (request,'display_Dept.html',d)

def display_EDJ(request):
    QLEDO=Emp.objects.all().select_related("DEPTNO")
    d={'QLEDO':QLEDO}
    return render(request,'display_EDJ.html',d)

def display_MEDJ(request):
    MEDJO=Emp.objects.all().select_related("DEPTNO").filter(SAL='5000')
    # MEDJO=Emp.objects.filter(ENAME="SMITH").select_related("DEPTNO")
    # MEDJO=Emp.objects.filter(JOB="MANAGER").select_related("DEPTNO")
    # MEDJO=Emp.objects.filter(COMM=None).select_related("DEPTNO")
    # MEDJO=Emp.objects.filter(HIREDATE="1981-05-01").select_related("DEPTNO")
    # MEDJO=Emp.objects.filter(DEPTNO__DNAME="ACCOUNTING").select_related("DEPTNO")
    # MEDJO=Emp.objects.filter(DEPTNO__LOC="CHICAGO").select_related("DEPTNO")
    # MEDJO=Emp.objects.filter().select_related("DEPTNO")
    d={'MEDJO':MEDJO}
    return render(request,'display_MEDJ.html',d)

def display_Lookups(request):
    # Lookups=Emp.objects.filter(ENAME__startswith='A').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__endswith='H').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__contains='I').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__gt='3000').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__lt='3000').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__gte='3000').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__lte='3000').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__in=['SMITH','ALLEN']).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__iexact='smith').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__istartswith='s').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__iendswith='h').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__icontains='i').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(JOB__in=['CLERK','SALESMAN']).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__DNAME__in=['RESEARCH','SALES']).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__LOC__in=['DALLAS','CHICAGO']).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__range=('2000','3000')).select_related("DEPTNO")
    # Lookups=Emp.objects.exclude(SAL__range=('2000','4000')).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__year__gt='1981').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__year__lt='1981').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__year__gte='1987').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__year__lte='1981'). select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__month__gt='05').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__month__lt='05').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__month__gte='05').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__month__lte='05').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__day__gt='01').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__day__lt='01').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__year='1981').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__month='05').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__day='01').select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__isnull=True).select_related("DEPTNO")
    #Lookups=Emp.objects.filter(ENAME__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(HIREDATE__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__DNAME__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__DNAME__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__LOC__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__LOC__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(MGR__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(MGR__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(COMM__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(COMM__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__isnull=True).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(DEPTNO__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(ENAME__isnull=False).select_related("DEPTNO")
    # Lookups=Emp.objects.filter(SAL__isnull=True).select_related("DEPTNO")
    Lookups=Emp.objects.filter(SAL__isnull=False).select_related("DEPTNO")
    d={'Lookups':Lookups}
    return render(request,'display_Lookups.html',d)

def display_EMO(request):
    QLEMO=Emp.objects.all().select_related("MGR")#display all details
    QLEMO=Emp.objects.all().select_related("MGR").filter(ENAME='SMITH')#display smith details only
    QLEMO=Emp.objects.all().select_related("MGR").filter(MGR__ENAME='BLAKE')# display employees who are having manager Blake
    QLEMO=Emp.objects.all().select_related("MGR").filter(MGR__isnull=True)# display employee who are not having manager
    QLEMO=Emp.objects.all().select_related("MGR").filter(MGR__isnull=False)#display employee who are having manager
    QLEMO=Emp.objects.all().select_related("MGR").filter(MGR__JOB='MANAGER')#display employee who's manager job is manager
    d={'QLEMO':QLEMO}
    return render(request,'display_EMO.html',d)

def display_EDMO(request):
    QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR")
    # QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR").filter(ENAME="ALLEN")
    # QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR").filter(DEPTNO__DNAME="SALES")
    # QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR").filter(DEPTNO__LOC="NEWYORK")
    # QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR").filter(MGR__isnull=True)
    # QLEDMO=Emp.objects.all().select_related("DEPTNO","MGR").filter(MGR__isnull=True)
    
    d={"QLEDMO":QLEDMO}
    return render(request,'display_EDMO.html',d)



def display_DERF(request):
    QLDEO=Dept.objects.all().prefetch_related('emp_set')
    # QLDEO=Dept.objects.prefetch_related('emp_set').filter(DNAME="SALES")
    # QLDEO=Dept.objects.prefetch_related('emp_set').filter(DNAME="ACCOUNTING")
    # QLDEO=Dept.objects.prefetch_related('emp_set').filter(DNAME="RESEARCH")
    
    d={"QLDEO":QLDEO}
    return render(request,'display_DERF.html',d)