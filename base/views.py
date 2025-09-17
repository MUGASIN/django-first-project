from django.shortcuts import render,HttpResponse,redirect
from base.models import Employee
from django.db.models import Q

# Create your views here.

def main(requst):

    details={
        'Employees':Employee.objects.all()
    }
    return render(requst,'main.html',details)


def delete_record(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()
    return redirect('main')


def create_record(request):

    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        desg=request.POST['designation']
        sal=request.POST['salary']
        Employee.objects.create(name=name,gender=gender,desg=desg,sal=sal)
        return redirect('main')
    else:
        return render(request,'emp_create.html')


def update_record(request,pk):
    emp=Employee.objects.get(id=pk)
    if request.method=='POST':
        emp=Employee.objects.get(id=pk)
        emp.name=request.POST.get('name')
        emp.gender=request.POST.get('gender')
        emp.desg=request.POST.get('designation')
        emp.sal=request.POST.get('salary')
        emp.save()
        return redirect('main')
        

    return render(request,'emp.update.html',{'emp':emp})


def search(request):
    if request.method=='GET':
        keyword=request.GET['word']
        details={
            'Employees': Employee.objects.all().filter(Q(name__contains=keyword) | Q(gender__contains=keyword) |Q(desg__contains=keyword) )
        }

    return render(request,'main.html',details)


def base(request):
    return redirect('main')