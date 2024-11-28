from django.urls import path
from . import views

app_name = 'product_api'

urlpatterns = [
    path('list/', views.ProductListApiView.as_view(), name='product-list-api'),
    path('brand/list/', views.BrandListApiView.as_view(), name='brand-list-api'),
]
