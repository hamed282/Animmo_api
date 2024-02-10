from rest_framework import serializers
from .models import UserCourseModel
from course.models import CourseModel


# class CourseSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(read_only=True, slug_field='category')
#     subcategory = serializers.SlugRelatedField(read_only=True, slug_field='subcategory')
#
#     class Meta:
#         model = CourseModel
#         fields = ['category', 'subcategory', 'course', 'teacher', 'season', 'duration']


class UserCourseSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='phone_number')
    # course = serializers.SlugRelatedField(read_only=True, slug_field='course')

    class Meta:
        model = UserCourseModel
        fields = ['user', 'course', 'spotplayer_license']

        depth = 1
