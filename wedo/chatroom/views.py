from django.shortcuts import render
from django.http import HttpRespone

# Create your views here.
def index(request):
    return HttpRespone('Hello Django!')