from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('register/verify/', views.RegisterVerifyCodeView.as_view(), name='user_register_verify'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('login/verify/', views.UserLoginVerifyView.as_view(), name='user_login_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', views.UserLogout.as_view(), name='token_logout'),

]
