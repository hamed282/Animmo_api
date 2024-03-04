from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserCourseSerializer
from .models import UserCourseModel
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MyCourseView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # user_id = self.request.query_params.get('user_id', None)
        user = get_object_or_404(User, id=request.user.id)
        my_course = UserCourseModel.objects.filter(user=user)
        ser_my_course = UserCourseSerializer(instance=my_course, many=True)

        return Response(data=ser_my_course.data)
