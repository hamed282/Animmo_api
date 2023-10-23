from rest_framework import serializers
from .models import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = CourseModel
        fields = '__all__'

