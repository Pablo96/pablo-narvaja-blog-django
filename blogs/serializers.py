from rest_framework.serializers import ModelSerializer
from .models import Blog, Tag

class TagSerializer(ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class BlogSerializer(ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'

    def to_internal_value(self, data):
        for tag in data['tags']:
            Tag.objects.get_or_create(name=tag)

        return super(BlogSerializer, self).to_internal_value(data)

class BlogPreviewSerializer(ModelSerializer):
    class Meta:
        model=Blog
        exclude=['content_html']
