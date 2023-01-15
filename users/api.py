from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

@api_view(['GET'])
def get_all_users(request: Request) -> Response:
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def sign_in(request: Request) -> Response:
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def sign_up(request: Request) -> Response:
    return Response(status=status.HTTP_200_OK)

class UserAPIView(APIView):
    def put(self, request: Request, blog_slug: str) -> Response:
        pass
    
    def delete(self, request: Request, blog_slug: str) -> Response:
        return Response(status=status.HTTP_200_OK)
