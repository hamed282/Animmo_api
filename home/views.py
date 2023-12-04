from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel
from blog.models import BlogModel
from .models import HeaderImageModel, FeedbackModel
from course.serializers import CourseCategorySerializer, CourseSubCategorySerializer, CourseSerializer,\
    SampleExerciseSerializer
from .serializers import HeaderImageSerializer, FeedbackSerializer
from blog.serializers import BlogSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class IndexView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        header_image = HeaderImageModel.objects.all()
        ser_header_image = HeaderImageSerializer(instance=header_image, many=True)

        course_category = CourseCategoryModel.objects.all()
        ser_course_category = CourseCategorySerializer(instance=course_category, many=True)

        course_subcategory = CourseSubCategoryModel.objects.all()
        ser_course_subcategory = CourseSubCategorySerializer(instance=course_subcategory, many=True)

        sample_exercise = SampleExerciseModel.objects.all()
        ser_sample_exercise = SampleExerciseSerializer(instance=sample_exercise, many=True)

        course = CourseModel.objects.all()
        ser_course = CourseSerializer(instance=course, many=True)

        feedback = FeedbackModel.objects.all()
        ser_feedback = FeedbackSerializer(instance=feedback, many=True)

        blog = BlogModel.objects.all()
        ser_blog = BlogSerializer(instance=blog, many=True)

        return Response(data=(ser_header_image.data, ser_course_category.data, ser_course_subcategory.data,
                              ser_course.data, ser_sample_exercise.data, ser_feedback.data, ser_blog.data))
