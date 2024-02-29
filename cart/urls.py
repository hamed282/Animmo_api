from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.CartAPI.as_view(), name='cart'),
    path('pay/', views.CartPayView.as_view(), name='pay'),
    path('zarin/verify/', views.CartPayVerify.as_view(), name='verify'),

]

