from rest_framework import serializers
from .models import HomeSettingModel, FeedbackModel, GuideModel


class HeaderImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeSettingModel
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='first_name')

    class Meta:
        model = FeedbackModel
        fields = '__all__'


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideModel
        fields = '__all__'
