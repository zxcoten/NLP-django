from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, )
# Create your views here.

def tokenz(request):
    return HttpResponse("<table>hello</table>")