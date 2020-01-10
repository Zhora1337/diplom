from django.urls import path
from .views import index, set_photo

urlpatterns = [
    path('', index, name='index'),
    path('photo/', set_photo, name='photo')
]
