from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    name = 'user'
    return HttpResponse("Hello " + name)
