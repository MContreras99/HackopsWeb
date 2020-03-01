from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return HttpResponse('about')
