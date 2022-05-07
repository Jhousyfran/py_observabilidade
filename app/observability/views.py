from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. %s" % time.strftime("%H:%M:%S") )
