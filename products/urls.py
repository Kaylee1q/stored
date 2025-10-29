from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Home page
    path('products/', views.products, name='products'),  # Products page
]
