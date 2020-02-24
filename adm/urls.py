from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.admIndex, name='admIndex'),
    path('new', views.calc_new, name='calc_new'),
    path('rand', views.calc_new, name='calc_rand'),
    path('started/<int:pk>/', views.calc_started, name='calc_started'),
    path('details/<int:pk>/', views.calc_details, name='calc_details'),
    path('download/<int:pk>/', views.calc_download, name='calc_download'),
    path('accounts/', include('django.contrib.auth.urls'), name='logInOut'),
]


