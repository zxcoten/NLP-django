from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')
# Create your views here.

def tokenz(request):
    return render(request, 'main/tokenz.html')

def normalize(request):
    return render(request, 'main/normalize.html')

def morphologic(request):
    return render(request, 'main/morpholog.html')