from rest_framework.views import APIView
from course.models import CourseModel
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserCourseSerializer
from .models import UserCourseModel
from django.shortcuts import get_object_or_404


class MyCourseView(APIView):
    def post(self, request):
        """
        parameters:
        1. phone_number
        """
        form = request.data
        phone_number = form['phone_number']
        user = get_object_or_404(User, phone_number=phone_number)
        my_course = UserCourseModel.objects.filter(user=user)
        # my_course = user.rel_user.all()
        ser_my_course = UserCourseSerializer(instance=my_course, many=True)

        return Response(data=ser_my_course.data)
