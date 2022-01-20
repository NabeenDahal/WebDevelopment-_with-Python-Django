from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('Welcome to homepage')

def aboutpageview(request):
    return HttpResponse('Welcome to aboutpage')

def contactpageview(request):
    return HttpResponse('Welcome to contactpage')

def blogpageview(request):
    return HttpResponse('Welcome to blogpage')
