from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_params', views.get_params, name='get_params'),
    path('search', views.search, name='search'),
]