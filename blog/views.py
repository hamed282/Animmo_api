from django.shortcuts import render
from rest_framework.views import APIView
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.response import Response


class BlogView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        blog = BlogModel.objects.all()
        ser_blog = BlogSerializer(instance=blog, many=True)

        return Response(data=ser_blog.data)
