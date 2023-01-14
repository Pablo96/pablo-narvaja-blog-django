from django.urls import path
from . import api

urlpatterns = [
    path('get/', api.get_all_tags),
    path('get/<str:blog_slug>', api.get_tag),
    path('create/<str:blog_slug>', api.create_tag),
]
