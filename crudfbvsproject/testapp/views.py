from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

def insert_view(request):
    form=EmployeeForm()
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})
def delete_view(request,id):
    employee= Employee.objects.get(id=id)
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation', '').lower()
        if confirmation == 'yes':
         employee.delete()
         return redirect('/')
        else:
         return redirect('/')
    return render(request,'testapp/delete.html')

def update_view(request,id):
    employee= Employee.objects.get(id=id)
    form=EmployeeForm(instance=employee)
    if request.method == 'POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})
    
def delete_all_view(request):
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation', '').lower()
        if confirmation == 'yes':
            Employee.objects.all().delete()
            return redirect('/')
        else:
            return redirect('/')
    return render(request,'testapp/deleteall.html')
    
    