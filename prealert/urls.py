from prealert import views
from django.urls import path

app_name = 'prealert'

urlpatterns = [
    path('prealert/', views.PreAlertView.as_view(), name='prealert'),
]