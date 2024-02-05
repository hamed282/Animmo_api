from django.urls import path
from . import views


app_name = 'user_panel'
urlpatterns = [
    path('', views.UserPanelView.as_view(), name='user_panel'),
]

