from django.urls import path

from .views import add_subscriber


urlpatterns = [
    path('add/', add_subscriber, name='add_subscriber'),
]