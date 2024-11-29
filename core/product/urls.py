from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('add-brand/', views.AddBrandView.as_view(), name='add-brand'),
    path('add-product/', views.AddProductView.as_view(), name='add-product'),

    path('report/brand/', views.BrandReport.as_view(), name='report-brand'),
    path('report/product/', views.ProductReport.as_view(), name='report-product'),
    path('report/made-in-nation-equal/',
         views.ProductMadeInNationEqualReport.as_view(), name='report-nation-made-in-equal'),
]
