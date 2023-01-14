from django.urls import path
from . import api

urlpatterns = [
    path('get/', api.get_all_blogs_previews),
    path('read/<str:blog_slug>', api.get_blog),
    path('write/<str:blog_slug>', api.create_or_update_blog),
]
