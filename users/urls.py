from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_all_users),
    path('sign-in/', api.sign_in),
    path('sign_up/', api.sign_up),
    path('<str:usr_email>/', api.UserAPIView.as_view()),
]
