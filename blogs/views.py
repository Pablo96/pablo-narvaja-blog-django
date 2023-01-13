from django.shortcuts import render
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from . import models
import json

def get_all_blogs_previews(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponseBadRequest('This url only supports GET http method')
    blog_previews = models.BlogPreview.objects.all().values()
    blog_previews_json_list = [blog.__dict__ for blog in blog_previews]
    return JsonResponse({"blogs": blog_previews_json_list})

def get_blog(request: HttpRequest, blog_slug: str) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponseBadRequest('This url only supports GET http method')
    try:
        blog = models.Blog.objects.get(pk=blog_slug)
        return JsonResponse(blog)
    except:
        return HttpResponseNotFound(f'blog "{blog_slug}" not found')


@login_required
def create_or_update_blog(request: HttpRequest, blog_slug: str) -> HttpResponse:
    if request.method != 'POST' or request.method != 'PUT':
        return HttpResponseBadRequest('This url only supports POST or PUT http methods')
    
    try:
        blog = models.Blog.objects.get(pk=blog_slug)
        #TODO: update the blog
        return HttpResponse(f'Updated blog "{blog_slug}"')
    except models.Blog.DoesNotExist:
        #TODO: create the blog
        return HttpResponse(f'Created blog "{blog_slug}"', status=201)
