from django.shortcuts import render

# Create your views here.

def index(request):
    """create the initial home page"""
    return render(request, 'home/index.html')