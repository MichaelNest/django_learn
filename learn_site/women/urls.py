from django.urls import path, re_path
from .views import index, cat, about, login, add_page, contact, show_post, show_category

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:cat_id>/', cat),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    # path('categories/<slug:cat>/', cat)
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]