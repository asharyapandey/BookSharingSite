from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from books.models import BookDetails, Request


@login_required(login_url='/users/login/')# decorator to allow acces to only logged in user
def profile(request, username):
    user = User.objects.get(username = username)
    user_books = BookDetails.objects.filter(added_by = user.id)
    #filter user requests joining tables/models
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
        try:#this is a check to see if the user with the same name is already registered
            user = User.objects.get(username = username)
            messages.warning(request, f'The Username is Already Taken.')
            return redirect('register')
        except User.DoesNotExist:
            user = User.objects.create_user(username = username, email = email, password = password)
            auth.login(request, user)#directly log in the user after registration
            messages.info(request, f'Registration Successfull')
            return redirect('register')

    return render(request, 'users/register.html')

def logout(request):
    auth.logout(request)
    return redirect('home_page')

def login(request):#view to check user login
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

def notification(request, username):
    #joined tables to get the incoming and users book requests
    accepted_requests = Request.objects.filter(requested_trade__added_by__id = request.user.id)
    incoming_requests = Request.objects.filter(requested_book__added_by__id = request.user.id)
    context = {
        'accepted_requests' : accepted_requests,
        'incoming_requests' : incoming_requests
    }
    if request.method == 'POST':
        #to accept or reject incoming book requests done using AJAX 
        is_accepted = request.POST['is_accepted']
        request_id = request.POST['request_id']
        this_request = Request.objects.get(id = request_id)
        if is_accepted == 'True':
            this_request.is_accepted = True
            this_request.is_declined = False
            this_request.save()
        else:
            this_request.is_declined = True
            this_request.is_accepted = False
            this_request.save()
        return redirect('notification', username = request.user.username)
    return render(request, 'users/notification.html', context)