from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse('Page of Women App')

def cat(request, cat_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by Categories</h1><p>{cat_id}</p>')

# def cat(request, cat):
#     return HttpResponse(f'<h1>Articles by Categories</h1><p>{cat}</p>')

def archive(request, year):
    if int(year)>2022:
        # raise Http404
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive for years</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>That Page is not Found!!!</h>')