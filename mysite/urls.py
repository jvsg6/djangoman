from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls), 
]

urlpatterns += i18n_patterns(
    path('', include('adm.urls')),
    path('', include('WindOro.urls')),
    path('', include('ManualSource.urls')),
    path('', include('MeteoForecast.urls')),
)
