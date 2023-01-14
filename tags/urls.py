from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_all_tags),
    path('<str:tag>/', api.TagAPIView.as_view()),
]
