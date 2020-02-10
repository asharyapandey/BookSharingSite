from django.shortcuts import render

def home_page(request):
    return render(request, 'home/index.html')#view for the home page
