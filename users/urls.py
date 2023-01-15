from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_all_users),
    path('sign_up/', api.sign_up),
    path('sign-in/', api.sign_in),
    path('sign-out/', api.sign_out),
    path('<str:usr_email>/', api.UserAPIView.as_view()),
]
