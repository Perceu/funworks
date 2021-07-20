from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'home.html')

# Create your views here.
def login(request):
    return render(request, 'login.html')