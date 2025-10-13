from django.urls import path
from . import views

urlpatterns = [
    path('web/', views.web, name='web'),
    path('home/', views.home, name='home'),
    path('product/<int:laptop_id>/', views.product_detail, name='product_detail'),
]