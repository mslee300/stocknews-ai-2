from django.contrib import admin
from django.urls import path, include
from stocknewsai.views import base_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocknewsai/', include('stocknewsai.urls')), 
    path('', base_views.index, name='index'),
]
