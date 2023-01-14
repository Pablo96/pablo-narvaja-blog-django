from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_all_blogs_previews),
    path('<str:blog_slug>/', api.BlogAPIView.as_view()),
]
