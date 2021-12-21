from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Page of Women App')

def cat(request):
    return HttpResponse('<h1>Articles by Categories</h1>')
