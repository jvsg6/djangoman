from django.urls import path

from . import views

urlpatterns = [
    path('', views.noscal, name='noscal'),
    path('new', views.calc_new, name='calc_new'),
    path('details/<int:pk>/', views.calc_detail, name='calc_detail'),
]
