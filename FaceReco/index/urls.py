from django.urls import path
from .views import index, set_photo, UpdateUserProfileView

urlpatterns = [
    path('', index, name='index'),
    path('photo/', set_photo, name='photo'),
    path('update/', UpdateUserProfileView.as_view()),
]
