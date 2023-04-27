from django.urls import path

from .views import base_views, subscribed_views

app_name = 'stocknewsai'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('subscribed/', subscribed_views.index, name='subscribed'),
]