from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import AboutSectionSerializer, AboutSectionToggleSerializer, FooterSerializer
from .models import AboutSection, Footer

@api_view(['GET'])
def get_active_sections(request: Request) -> Response:
    active_sections = AboutSection.objects.filter(active=False)
    about_section_serializer = AboutSectionSerializer(active_sections, many=True)
    active_sections = about_section_serializer.data
    return Response(data=active_sections, status=status.HTTP_200_OK)

@api_view(['PUT'])
def toggle_active_section(request: Request, section_name: str) -> Response:
    section = AboutSection.objects.filter(pk=section_name).first()
    if section is None:
        return Response(data=f'About section "{section_name}" not found', status=status.HTTP_404_NOT_FOUND)
    section.active = not section.active
    section.save()
    about_section_serializer = AboutSectionToggleSerializer(section)
    return Response(data=about_section_serializer.data, status=status.HTTP_200_OK)

class AboutSectionAPIView(APIView):
    def get(self, request: Request, section_name: str) -> Response:
        section = AboutSection.objects.filter(pk=section_name).first()
        if section is None:
            return Response(data=f'About section "{section_name}" not found', status=status.HTTP_404_NOT_FOUND)
        about_section_serializer = AboutSectionSerializer(section)
        section = about_section_serializer.data
        return Response(data=section, status=status.HTTP_200_OK)

    def post(self, request: Request, section_name: str) -> Response:
        existing_section = AboutSection.objects.filter(pk=section_name).first()
        should_insert = existing_section == None

        if not should_insert:
            return Response(f'About section "{section_name}" already exists, use PUT method to update it', status=status.HTTP_400_BAD_REQUEST)

        about_section_serializer = AboutSectionSerializer(data=request.data)
        if not about_section_serializer.is_valid():
          return Response(data=about_section_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            about_section_serializer.validated_data.name=section_name
            about_section_serializer.save()
            return Response(f'Created about section "{section_name}"', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    def put(self, request: Request, section_name: str) -> Response:
        existing_section = AboutSection.objects.filter(pk=section_name).first()
        should_insert = existing_section == None

        if should_insert:
            return Response(f'About section "{section_name}" does not exists, use POST method to create it', status=status.HTTP_400_BAD_REQUEST)

        about_section_serializer = AboutSectionSerializer(existing_section, data=request.data)
        response = Response(f'Updated about section "{section_name}"', status=status.HTTP_200_OK)

        if not about_section_serializer.is_valid():
          return Response(data=about_section_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            about_section_serializer.save()
            return response
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: Request, section_name: str) -> Response:
        try:
            AboutSection.objects.filter(pk=section_name).delete()
            return Response(data=f'Deleted about section "{section_name}"', status=status.HTTP_200_OK)
        except:
            return Response(data=f'About section "{section_name}" not found', status=status.HTTP_404_NOT_FOUND)

class FooterAPIView(APIView):
    def get(self, request: Request, footer_id: str) -> Response:
        footer = Footer.objects.filter(pk=footer_id).first()
        if footer is None:
            return Response(data=f'Footer "{footer_id}" not found', status=status.HTTP_404_NOT_FOUND)
        footer_serializer = FooterSerializer(footer)
        footer = footer_serializer.data
        return Response(data=footer, status=status.HTTP_200_OK)

    def post(self, request: Request, footer_id: str) -> Response:
        existing_footer = Footer.objects.filter(pk=footer_id).first()
        should_insert = existing_footer == None

        if not should_insert:
            return Response(f'Footer "{footer_id}" already exists, use PUT method to update it', status=status.HTTP_400_BAD_REQUEST)

        footer_serializer = FooterSerializer(data=request.data)
        if not footer_serializer.is_valid():
          return Response(data=footer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            footer_serializer.save()
            return Response(f'Created footer "{footer_id}"', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    def put(self, request: Request, footer_id: str) -> Response:
        existing_footer = Footer.objects.filter(pk=footer_id).first()
        should_insert = existing_footer == None

        if should_insert:
          footer_serializer = FooterSerializer(data=request.data)
          response = Response(f'Created footer "{footer_id}"', status=status.HTTP_201_CREATED)
        else:
          footer_serializer = FooterSerializer(existing_footer, data=request.data)
          response = Response(f'Updated footer "{footer_id}"', status=status.HTTP_200_OK)

        if not footer_serializer.is_valid():
          return Response(data=footer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            footer_serializer.save()
            return response
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: Request, footer_id: str) -> Response:
        try:
            Footer.objects.filter(pk=footer_id).delete()
            return Response(data=f'Deleted footer "{footer_id}"', status=status.HTTP_200_OK)
        except:
            return Response(data=f'Footer "{footer_id}" not found', status=status.HTTP_404_NOT_FOUND)
