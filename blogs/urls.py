from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_all_blogs_previews),
    path('read/<str:slug>', views.get_blog),
    path('post/<str:slug>', views.create_blog),
]
