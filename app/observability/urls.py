from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error', views.pageerror, name='pageerror'),
    path('api', views.api, name='api'),
]