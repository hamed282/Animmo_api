from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CourseViewSerializer
from .models import CourseModel
# # from .serializers import CourseSubcategoryListSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class CourseCategoryListView(APIView):
#     def get(self, request):
#         category = CourseCategoryModel.objects.get(category='سه بعدی')
#         product = CourseSubCategoryModel.objects.filter(category=category)
#         ser_product = CourseSubcategoryListSerializer(instance=product, many=True)
#
#         # subcategory =
#         count_course = CourseModel.objects.filter(subcategory=)
#         print(product)
#         return Response(data=ser_product.data)

# class AddCartView(APIView):
#     authentication_classes = [JWTAuthentication]
#
#     def post(self, request):
#         """
#         parameters:
#         1. course
#         2. price
#         """
#         form = request.data
#         ser_data = OrderItemSerializer(data=form)
#         if ser_data.is_valid():
#
#             paid_check = OrderModel.objects.filter(user=request.user, paid=False).exists()
#             if not paid_check:
#                 OrderModel.objects.create(user=request.user)
#
#             course = CourseModel.objects.get(course=ser_data.validated_data['course'])
#             exist_course = OrderItemModel.objects.filter(course=course).exists()
#             if not exist_course:
#                 price = ser_data.validated_data['price']
#                 order = OrderModel.objects.get(user=request.user)
#                 OrderItemModel.objects.create(order=order, course=course, price=price)
#             else:
#                 pass
#         order = OrderModel.objects.get(user=request.user, paid=False)
#         orders = OrderItemModel.objects.filter(order=order).all()
#
#         ser_order = OrderItemSerializer(instance=orders, many=True)
#
#         return Response(data=(ser_order.data, {'total_price': order.get_total_price()}))


class ViewCourseView(APIView):
    def get(self, request):
        course_id = self.request.query_params.get('id', None)
        course = get_object_or_404(CourseModel, id=course_id)
        ser_course = CourseViewSerializer(instance=course)

        return Response(data=ser_course.data)
