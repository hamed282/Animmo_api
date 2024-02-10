from django.urls import path
from . import views


app_name = 'user_panel'
urlpatterns = [
    path('my_course/', views.MyCourseView.as_view(), name='my_course'),
]
