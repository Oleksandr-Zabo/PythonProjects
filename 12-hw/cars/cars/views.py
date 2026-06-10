from django.shortcuts import render

def home(request):
    return render(request, 'cars/home.html')

def toyota(request):
    return render(request, 'cars/toyota.html')

def honda(request):
    return render(request, 'cars/honda.html')

def renault(request):
    return render(request, 'cars/renault.html')
