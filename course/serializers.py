from rest_framework import serializers
from .models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel, OrderModel,\
    OrderItemModel


# class CourseSubcategoryListSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(slug_field='category', read_only=True)
#
#     class Meta:
#         model = CourseModel
#         fields = ['category', 'subcategory', 'image']


class CourseCategorySerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = CourseCategoryModel
        fields = '__all__'


class CourseSubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    count_course = serializers.SerializerMethodField()

    class Meta:
        model = CourseSubCategoryModel
        fields = '__all__'

    def get_count_course(self, obj):
        count_course = CourseModel.objects.filter(subcategory=obj.id).count()

        return count_course



class CourseSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = CourseModel
        fields = '__all__'


class SampleExerciseSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    subcategory = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    user = serializers.SlugRelatedField(read_only=True, slug_field='last_name')

    class Meta:
        model = SampleExerciseModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    get_total_price = serializers.CharField()

    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderItemSerializer(serializers.Serializer):
    # class Meta:
    #     model = OrderItemModel
    #     fields = ['price']
    price = serializers.CharField()
    course = serializers.CharField()


