from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is a second_app home page.')

def courses(request):
    return HttpResponse('This is a second_app course')

def about(request):
    return HttpResponse('This is second_app about section')
