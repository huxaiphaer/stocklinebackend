from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.RegisterAPIView.as_view(), name='create'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]

