from django.urls import path, re_path
from .views import index, cat, archive

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:cat_id>/', cat),
    # path('categories/<slug:cat>/', cat)
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]