"""pablo_narvaja_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import api

urlpatterns = [
    path('about/', api.get_active_sections),
    path('about/<str:section_name>/', api.AboutSectionAPIView.as_view()),
    path('about/toggle_active/<str:section_name>/', api.toggle_active_section),
    path('footer/<str:footer_id>/', api.FooterAPIView.as_view()),
]
