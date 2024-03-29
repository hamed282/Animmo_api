from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='home')
    path('home_setting/', views.HeaderImageView.as_view(), name='home_setting'),
    path('course_category/', views.CourseCategoryView.as_view(), name='course_category'),
    path('course_subcategory/', views.CourseSubcategoryView.as_view(), name='course_subcategory'),
    path('sample_exercise/', views.SampleExerciseView.as_view(), name='sample_exercise'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('guide/', views.GuideView.as_view(), name='guide'),
]

