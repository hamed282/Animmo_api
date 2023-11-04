from rest_framework import serializers
from .models import HeaderImageModel, FeedbackModel


class HeaderImageSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = HeaderImageModel
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='first_name')

    class Meta:
        model = FeedbackModel
        fields = '__all__'
