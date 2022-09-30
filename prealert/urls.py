from prealert import views
from django.urls import path

app_name = 'prealert'

urlpatterns = [
    path('prealert/', views.PreAlertView.as_view(), name='prealert'),
    path('weigh-bridge/', views.WeighBridgeView.as_view(), name='weigh-bridge'),
    path('weigh-bridge/<int:id>/', views.WeighBridgeView.as_view(),
         name='weigh-bridge-detail'),
    path('holding-certificate/', views.GuaranteedGoodsView.as_view(),
         name='holding-certificate'),
    path('holding-certificate/<int:id>/', views.GuaranteedGoodsView.as_view(),
         name='holding-certificate'),
    # path('search_holding_certificate/',
    #      views.search_housing_certificate_view,
    #      name='search-housing-certificate'),
    path('prealert/<int:id>/',
         views.PreAlertDetail.as_view(), name='prealert-details'),
]
