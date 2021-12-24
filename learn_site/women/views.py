from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from women.models import Women


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Выйти', 'url_name': 'login'}]

def index(request):
    posts = Women.objects.all()
    context = {'posts': posts, 'menu': menu, 'title': 'Master Page'}
    # return HttpResponse('Page of Women App')
    return render(request, 'women/index.html', context=context)

def about(request):
    context = {'menu': menu, 'title': 'About Site'}
    return render(request, 'women/about.html', context=context)

def add_page(request):
    # context = {'menu': menu,}
    # return render(request, 'women/add_page.html', context=context)
    return HttpResponse('<h2>Add Page</h2>')

def login(request):
    # context = {'menu': menu,}
    # return render(request, 'women/login.html', context=context)
    return HttpResponse('<h2>Log in</h2>')

def contact(request):
    # context = {'menu': menu,}
    # return render(request, 'women/contact.html', context=context)
    return HttpResponse('<h2>Our Contacts</h2>')

def show_post(request, post_id):
    # context = {'menu': menu, 'post_id': post_id}
    # return render(request, 'women/show_post.html', context=context)
    return HttpResponse(f'<h2>Identeficator number is {post_id}</h2>')

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