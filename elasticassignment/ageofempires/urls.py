from django.urls import path
from . import views

urlpatterns = [
    path('', views.civilizations, name='civilizations'),
    path('civilizations', views.civilizations, name='civilizations'),
    path('units', views.units, name='units'),
    path('structures', views.structures, name='structures'),
    path('technologies', views.technologies, name='technologies'),
]
