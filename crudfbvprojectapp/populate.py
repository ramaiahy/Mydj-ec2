import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvprojectapp.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
fakegen=Faker()
def populate(n): 
 for i in range(n):
    feno=randint(1001,9999)
    fename=fakegen.name()
    fesal=randint(10000,20000)
    feadd=fakegen.city()
    emp_record =Employee.objects.get_or_create(
        eno=feno,
        ename=fename,
        esal=fesal,
        eaddr=feadd
    )
n=int(input('Enter no of records'))
populate(n)
print(f'{n} Records inserted succussfully')
