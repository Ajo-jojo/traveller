from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect("login")

    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['pass']
        conpass = request.POST['conpass']

        if password==conpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"THIS USERNAME IS ALREADY TAKEN.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"THIS EMAIL ID  IS ALREADY TAKEN.")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,
                                      password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"PASSWORDS DOESN'T MATCH. "
                                  " PLEASE TRY AGAIN.")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

