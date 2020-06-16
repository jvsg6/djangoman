from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [

    path('new', views.calc_new, name='calc_new'),
    path('rand', views.calc_rand, name='calc_rand'),
    path('edit/<int:pk>/', views.calc_edit, name='calc_edit'),
    path('started/<int:pk>/', views.calc_started, name='calc_started'),
    path('full_wind_parameters/add/', views.addFullWindParameters, name='addFullWindParameters'),
    path('details/<int:pk>/', views.calc_details, name='calc_details'),
    path('download/<int:pk>/', views.calc_download, name='calc_download'),
    path('accounts/', include('django.contrib.auth.urls'), name='logInOut'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    path('', views.admListPart, name='admListPart'),
    path('all/', views.admListPart, name='admListPart'),
    path('all/<int:pagId>/', views.admListPart, name='admListPart'),
]


