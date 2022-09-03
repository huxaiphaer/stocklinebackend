from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('customer/', views.CustomerView.as_view(), name='customer'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('packaging/', views.PackagingView.as_view(), name='packaging'),
    path('product/<int:id>/packaging',
         views.PackagingDetail.as_view(), name='packaging'),
]
