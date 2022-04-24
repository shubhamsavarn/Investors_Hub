from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib import messages
from app1.forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def register(request):
    if request.method == "POST":
        print(request.method)
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            print('sucess')
            inputUsername = fm['username'].value()
            inputPass = fm['password'].value()
            inputEmail = fm['email'].value()
            user = User.objects.create_user(
            username=inputUsername, password=inputPass, email=inputEmail)
            messages.success(request, 'Form submission successful')
            print(user)
        else:
            print("fuck")
    else:
        fm = SignUpForm()
    return render(request,'app1/register.html',{'fm1':fm})
#login
def auth_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          print('sucess')
          user = authenticate(username=uname,password=upass)
          if user is not None:
            login(request,user)
            return HttpResponseRedirect('/profile/')
        else:
            print("not done")
    else:
        fm = AuthenticationForm() 
    return render(request,'app1/login.html',{'fm1':fm})

#profile after login

def profile(request):
    return render(request,'app1/profile.html')


#chnage password (profile)

def user_profile(request):
    return render(request,'app1/profile2.html')

#change pass
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            print("omg")
    else:
        form = PasswordChangeForm(user=request.user)
        print("fuck")


    return render(request, 'app1/chngpass.html', {
        'fm1': form,
    })
