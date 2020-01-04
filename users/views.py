from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

def register(request ):
    if request.method == 'POST':
        username = request.POST['username']
        welcome = f'welcome to the site Mr. {username}'
        return JsonResponse({"data" : welcome})

    return JsonResponse({'data' : 'ayena'})
