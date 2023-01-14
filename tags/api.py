from rest_framework.views import APIView
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

class TagAPIView(APIView):
    def get(self, request: Request, tag: str) -> Response:
        tag_obj = Tag.objects.filter(name=tag).first()
        if tag_obj is None:
            return Response(data=f'Tag "{tag}" not found', status=status.HTTP_404_NOT_FOUND)
        
        tag_serializer = TagSerializer(tag_obj)
        tag = tag_serializer.data
        return Response(data=tag, status=status.HTTP_200_OK)

    def post(self, request: Request, tag: str) -> Response:
        _ = Tag.objects.get_or_create(name=tag)
        return Response(data=f'Tag "{tag}" created', status=status.HTTP_201_CREATED)

    def delete(self, request: Request, tag: str) -> Response:
        try:
            _ = Tag.objects.filter(pk=tag).delete()
            return Response(data=f'Tag "{tag}" deleted', status=status.HTTP_200_OK)
        except:
            return Response(data=f'Tag "{tag}" not found', status=status.HTTP_404_NOT_FOUND)
        