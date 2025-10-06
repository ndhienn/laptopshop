from django.urls import path
from . import views

urlpatterns = [
    path('Web/', views.Web, name='Web'),
    path('product/', views.product, name='product')
]