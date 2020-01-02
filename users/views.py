from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        print(request.POST['username'])

    return render(request, 'users/profile.html')
