from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import TagSerializer
from .models import Tag

@api_view(['GET'])
def get_all_tags(request: Request) -> Response:
    tags = Tag.objects.all()
    tag_serializer = TagSerializer(tags, many=True)
    tags = tag_serializer.data
    return Response(data=tags, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_tag(request: Request, tag: str) -> Response:
    tag = Tag.objects.filter(name=tag).first()
    if tag is None:
        return Response(data=f'Tag "{tag}" not found', status=status.HTTP_404_NOT_FOUND)
    
    tag_serializer = TagSerializer(tags, many=True)
    tags = tag_serializer.data
    return Response(data=tags, status=status.HTTP_200_OK)

@api_view(['GET'])
def create_tag(request: Request, tag: str) -> Response:
    _ = Tag.objects.create(name=tag)
    return Response(data=f'Tag "{tag}" created', status=status.HTTP_201_OK)