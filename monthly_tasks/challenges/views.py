from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def jan(req):
   return HttpResponse("hello world")
