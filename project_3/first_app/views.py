from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'Sharif', 'age': 5, 'lst':['python', 'is', 'best'], 'birthday': datetime.datetime.now(), 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 1000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee': 2000
        }
    ]}
    return render(request, 'home.html', d)