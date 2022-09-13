from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")     
            return redirect('/')

    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})     


def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        username = request.POST.get('username') 
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
             messages.error(request, "User does not exist")     

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")  
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})        
      
def logout_user(request):
    logout(request)
    messages.info(request, "User loged out")
    return redirect('/')
