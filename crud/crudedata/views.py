from django.shortcuts import render
from .models import student
from .forms import loginForm
from django.http import HttpResponseRedirect

def index(request):
  
    fm = loginForm()
    # getting the data 
    info = student.objects.all()
    if request.method == 'POST':
        fm = loginForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            usn = fm.cleaned_data['usn']
            password = fm.cleaned_data['password']
            reg =student(name =name, usn =usn, password =password)
            reg.save()
            fm  = loginForm()
    else : 
        fm = loginForm()        
    return render(request, 'index.html',{'fm':fm,'info' : info,'edit':True})
# Create your views here.


# deleting the data
def deleteData(request,data):
    # print(data) data = "it is a  saved information in dbs for a user"
    info = student.objects.get(pk=data)
    info.delete()
    return HttpResponseRedirect('/')


# for upadating data  
def updateData(request,data):
    info = student.objects.get(pk=data)
    # fm = loginForm(initial = {'name' : info.name, 'usn' : info.usn ,'password' : info.password})
    if request.method == 'POST':
        fm = loginForm(request.POST) 
        if fm.is_valid():
            name = fm.cleaned_data['name']
            usn = fm.cleaned_data['usn']
            password = fm.cleaned_data['password']
            reg = student(id=data,name=name,usn=usn,password=password)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = loginForm(initial = {'name' : info.name, 'usn' : info.usn ,'password' : info.password})
        return render(request, 'index.html',{'fm':fm,'edit' :False ,'name' : info.name , 'info' : info})

        
        
    