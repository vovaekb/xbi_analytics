from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics_index, name='analytics_index'),
]

