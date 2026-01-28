from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.product, name='product'),
    path('product<int:id>', views.product_details, name='product_details'),
]
