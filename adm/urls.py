from django.urls import path

from . import views

urlpatterns = [
    path('', views.admIndex, name='admIndex'),
    path('new', views.calc_new, name='calc_new'),
    path('details/<int:pk>/', views.calc_detail, name='calc_detail'),
]
