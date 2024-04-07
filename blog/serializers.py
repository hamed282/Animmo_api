from rest_framework import serializers
from blog.models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='full_name')

    class Meta:
        model = BlogModel
        fields = '__all__'
