from django.db import models
from rest_framework import fields,serializers
from home.models import Visit

class Visitserilizer(serializers.Serializer):
    fromdate = serializers.CharField(max_length=30)
    todate = serializers.CharField(max_length=30)
    noofguest = serializers.CharField(max_length=30)
    typeofacc = serializers.CharField(max_length=30)