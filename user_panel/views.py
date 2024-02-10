from rest_framework.views import APIView
from course.models import CourseModel
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserCourseSerializer
from .models import UserCourseModel
from rest_framework import generics


class MyCourseView(APIView):
    def get(self, request):
        user = User.objects.get(phone_number='09129262249')
        my_course = UserCourseModel.objects.filter(user=user)
        # my_course = user.rel_user.all()
        ser_my_course = UserCourseSerializer(instance=my_course, many=True)

        return Response(data=ser_my_course.data)
