from rest_framework.views import APIView
from rest_framework.response import Response
from course.models import CourseModel
from course.serializers import CourseSerializer


class IndexView(APIView):
    def get(self, request):
        courses = CourseModel.objects.all()
        ser_data = CourseSerializer(instance=courses, many=True)
        return Response(data=ser_data.data)
