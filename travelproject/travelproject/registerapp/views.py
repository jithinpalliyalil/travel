from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import redirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        uname = request.POST['user name']
        password = request.POST['password']
        password1 = request.POST['confirm password']

        if password==password1:
            if User.objects.filter(email=email).exists():
                 messages.info(request,"email taken")
                 return redirect('register')
            elif User.objects.filter(username=uname).exists():
                 messages.info(request,"username taken")
                 return redirect('register')

            else:
                 user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
                 user.save();
                 messages.info(request,"user created")
                 return redirect(request,'login')
        else:
             messages.info(request,"password not match")
             return redirect('register')

    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']

        User.auth.authenticate(username=uname,password=password)

        if User is not None:
            auth.login(request,User)
            return redirect(request,'/')
        else:
            messages.info(request,"invalid register")
            return redirect(request,'login/')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect(request,'/')