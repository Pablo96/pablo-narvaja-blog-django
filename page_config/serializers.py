from rest_framework.serializers import ModelSerializer
from .models import Footer, AboutSection

class AboutSectionSerializer(ModelSerializer):
    class Meta:
        model=AboutSection
        exclude=['active']

class FooterSerializer(ModelSerializer):
    class Meta:
        model=Footer
        fields='__all__'

