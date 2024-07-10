from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserDetailsForm, studentForm
from .models import UserDetails, StudentData


def home(request):
    return render(request,'home.html')



def userregistration(request):
    if request.method=='POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            mobile=request.POST.get('mobile')
            address=request.POST.get('address')
            if password == confirmpassword:
                user = User.objects.create_user(username=name, email=email, password=password)
                UserDetails.objects.create(mobile=mobile,address=address,user=user)
                send_mail('Thank you '+name+' for registration',
                          'Here is your login Below \nhttp://127.0.0.1:8000/index/',
                          settings.EMAIL_HOST_USER,
                          [email]
                          )
                return redirect('/login/')
    form = UserDetailsForm()
    return render(request, 'registration.html', {'form': form})




def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
           login(request,user)
           return redirect('/index/')
        else:
            return render(request, 'userlogin.html',{'comment': 'Enter Valid details'})
    return render(request,'userlogin.html')




def  index(request):
    student_data=StudentData.objects.all()
    details={'std_data':student_data}
    return render(request,'index.html',details)




def user_logout(request):
    logout(request)
    return redirect('/login/')


def create(request):
    if request.method=='POST':
        print(request.POST)
        form=studentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
            form=studentForm()
    return render(request,'create.html',{'form':form})

def edit(request,id):
    emp_data = StudentData.objects.get(id=id)
    form=studentForm(instance=emp_data)
    return render(request,"update.html",{'form':form,'id':id})


def update(request,id):
    std_data = StudentData.objects.get(id=id)
    form= studentForm(request.POST,instance=std_data)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,"update.html", {'form':form,'id':id})

def delete(request,id):
    std_data=StudentData.objects.get(id=id)
    std_data.delete()
    return redirect('/index/')








