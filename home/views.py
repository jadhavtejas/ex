from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from home.models import Book

# Create your views here.


def index(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('last_name')
        number = request.POST.get('number')
        # return HttpResponse(firstname)
        Visit111 = Book(firstname = firstname,lastname=lastname,number=number)
        Visit111.save()

    data = {
        "title": 'Login',
        "headding": "Login",
    }
    return render(request, 'HTML/index.html', data)


# def home(request):
#     data = {
#         "title": 'AgroFarm',
#         "headding": "AgroFarm",
#     }
#     return render(request, '../templates/HTML/home.html', data)


def contact(request):
    return HttpResponse('This is contact page')
