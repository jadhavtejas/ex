from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import serializers
from baapagro.home.serializer import Visitserilizer
from home.models import Visit
from rest_framework.renderers import JSONRenderer

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
    return render(request, 'HTML/index.html', data)


def contact(request):
    # return HttpResponse("Hello!! I am on contact~!")
    return render(request, 'HTML/login.html')

def Visit_details(request):
    #collecting the data
    visit_details = Visit.get(id=1)
    serializer_data = Visitserilizer(visit_details)

    json_data = JSONRenderer().render(serializer_data)
    return HttpResponse(json_data)