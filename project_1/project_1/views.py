from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the home page")
def contack(request):
    return HttpResponse("This is the contact page")