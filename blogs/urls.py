from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_all_blogs_previews),
    path('read/<str:blog_slug>', views.get_blog),
    path('post/<str:blog_slug>', views.create_or_update_blog),
]
