from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from books.models import BookDetails, Request


@login_required(login_url='/users/login/')
def profile(request, username):
    user = User.objects.get(username = username)
    user_books = BookDetails.objects.filter(added_by = user.id)
    user_requests = Request.objects.filter(requested_trade__added_by__id = user.id)
    context = {
        'books' : user_books,
        'user_requests' : user_requests
    }
    return render(request, 'users/profile.html', context)


def register(request ):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
            messages.warning(request, f'The Username is Already Taken.')
            return redirect('register')
        except User.DoesNotExist:
            user = User.objects.create_user(username = username, email = email, password = password)
            auth.login(request, user)
            messages.warning(request, f'Registration Successfull')
            return redirect('register')

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
            return redirect('home_page')
        else:
            messages.warning(request, f'Login not Succesful')
            return redirect('login')
    
    return render(request, 'users/login.html')


def update(request, id):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.get(id = id)
        user.username = username
        user.email = email
        user.save()
        return redirect('profile')

    return render(request, 'users/register.html')