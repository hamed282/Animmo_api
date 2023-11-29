from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('add_cart/', views.AddCartView.as_view(), name='add_cart')
]
