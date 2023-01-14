from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, BlogPreviewSerializer
from .models import Blog

@api_view(['GET'])
def get_all_blogs_previews(request: Request) -> Response:
    tags = request.query_params.getlist('tag')
    if tags is not None and len(tags) > 0:
      blogs_previews = Blog.objects.defer('content_html').filter(tags__in=tags)
    else:
       blogs_previews = Blog.objects.defer('content_html').all()
    blogs_previews_serializer = BlogPreviewSerializer(blogs_previews, many=True)
    blogs_previews = blogs_previews_serializer.data
    return Response(data=blogs_previews, status=status.HTTP_200_OK)

class BlogAPIView(APIView):
    def get(self, request: Request, blog_slug: str) -> Response:
        blog = Blog.objects.filter(pk=blog_slug).first()
        if blog is None:
            return Response(data=f'Blog "{blog_slug}" not found', status=status.HTTP_404_NOT_FOUND)
        blog_serializer = BlogSerializer(blog)
        blog = blog_serializer.data
        return Response(data=blog, status=status.HTTP_200_OK)

    def post(self, request: Request, blog_slug: str) -> Response:
        prev_blog = Blog.objects.filter(pk=blog_slug).first()
        should_insert = prev_blog == None

        if not should_insert:
            return Response(f'Blog "{blog_slug}" already exists, use PUT method to update it', status=status.HTTP_400_BAD_REQUEST)

        blog_serializer = BlogSerializer(data=request.data)
        if not blog_serializer.is_valid():
          return Response(data=blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            blog_serializer.validated_data.slug=blog_slug
            blog_serializer.save()
            return Response(f'Created blog "{blog_slug}"', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    def put(self, request: Request, blog_slug: str) -> Response:
        prev_blog = Blog.objects.filter(pk=blog_slug).first()
        should_insert = prev_blog == None

        if should_insert:
            return Response(f'Blog "{blog_slug}" does not exists, use POST method to create it', status=status.HTTP_400_BAD_REQUEST)
    
        blog_serializer = BlogSerializer(prev_blog, data=request.data)
        response = Response(f'Updated blog "{blog_slug}"', status=status.HTTP_200_OK)

        if not blog_serializer.is_valid():
          return Response(data=blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            blog_serializer.save()
            return response
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: Request, blog_slug: str) -> Response:
        try:
            Blog.objects.filter(pk=blog_slug).delete()
            return Response(data=f'Deleted blog "{blog_slug}"', status=status.HTTP_200_OK)
        except:
            return Response(data=f'Blog "{blog_slug}" not found', status=status.HTTP_404_NOT_FOUND)
