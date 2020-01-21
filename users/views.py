from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def register(request ):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
            return JsonResponse({"success": "false", "data" : "The Username is Already Taken."})
        except User.DoesNotExist:
            user = User.objects.create_user(username = username, email = email, password = password)
            auth.login(request, user)
            return JsonResponse({"success": "true", "data" : "Registration Successfull"})

    return render(request, 'users/register.html')

def logout(request):
    auth.logout(request)
    return redirect('home_page')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Login Succesful')
            #return JsonResponse({"success": "true", "data" : "Log In Successful."})
            return redirect('home_page')
        else:
            #return JsonResponse({"success": "false", "data" : "Invalid Credentials."})
            messages.warning(request, f'Login not Succesful')
            return redirect('home_page')
    
    return render(request, 'users/login.html')


def profile(request):
    return render(request, 'users/profile.html')