from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import serializers
from home.serializer import Visitserilizer
from home.models import Visit
from rest_framework.renderers import JSONRenderer
import requests

# Create your views here.


def index(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        noofguest = request.POST.get('noofguest')
        typeofacc = request.POST.get('typeofacc')
        # return HttpResponse(fromdate)
        Visit111 = Visit(fromdate=fromdate, todate=todate,
                         noofguest=noofguest, typeofacc=typeofacc)
        Visit111.save()

    data = {
        "title": "Home Page",
        "description": "BAAP AGRO!!!"
    }
    # return HttpResponse("Hello!! I am on homepage")
    return render(request, 'HTML/login.html', data)


def contact(request):
    # return HttpResponse("Hello!! I am on contact~!")
    return render(request, 'HTML/login.html')


def Visit_details(request, pk):
    # collecting the data
    visit_details = Visit.objects.get(id=pk)
    serializer_data = Visitserilizer(visit_details)
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data)


def Visit_list(requests):
    visit_details = Visit.objects.all()
    serializer_data = Visitserilizer(visit_details, many=True)
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data)


def VisitData(request):
    url = 'http://127.0.0.1:8000/visit_list/'
    r = requests.get(url=url)
    data = r.json()
    return render(request, 'HTML/display.html', {'response': data})


def login(request):
    return render(request,'HTML/login.html')


def register(request):
    return render(request,'HTML/register.html')

def main(request):
    return render(request,'HTML/index.html')