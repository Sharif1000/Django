from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is a first_app home page.')

def courses(request):
    return HttpResponse('This is a first_app course')

def about(request):
    return HttpResponse('This is first_app about section')
