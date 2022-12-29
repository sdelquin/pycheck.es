from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('version/', views.version, name='version'),
    path('login/', views.login, name='login'),
    ]
