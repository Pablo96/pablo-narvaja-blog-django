from rest_framework.serializers import ModelSerializer
from .models import Footer, AboutSection

class AboutSectionSerializer(ModelSerializer):
    class Meta:
        model=AboutSection
        exclude=['active']


class AboutSectionToggleSerializer(ModelSerializer):
    class Meta:
        model=AboutSection
        fields='__all__'

class FooterSerializer(ModelSerializer):
    class Meta:
        model=Footer
        fields='__all__'

