from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def jan(req):
   return HttpResponse("jan hello")

def feb(req):
   return HttpResponse("feb hello")