from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def get_all_blogs_previews(request):
    return HttpResponse('All blogs previews')

def get_blog(request):
    return HttpResponse('A blog')

@login_required
def create_or_update_blog(request):
    return HttpResponse('Created or Updated')
