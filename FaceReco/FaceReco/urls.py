"""FaceReco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import StreamingHttpResponse
from django.urls import path, include
from camera import VideoCamera, gen, VideoCamera2
from rest_framework.authtoken import views as authviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),
    path('monitor2/', lambda r: StreamingHttpResponse(gen(VideoCamera2()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),                                               
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', authviews.obtain_auth_token),
]
