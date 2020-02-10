from django.urls import path

from . import views

urlpatterns = [
    path('', views.admIndex, name='admIndex'),
    path('new', views.calc_new, name='calc_new'),
    path('started/<int:pk>/', views.calc_started, name='calc_started'),
    path('details/<int:pk>/', views.calc_details, name='calc_details'),
]
