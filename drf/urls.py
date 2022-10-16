"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import re_path, include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from face import views

router = DefaultRouter()
router.register(r'face/upload/image', views.ImageViewSet)
router.register(r'face/upload/video', views.VideoViewSet)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
    path(r'api/face/image/<str:filename>/', views.ImageDownloadViewSet),
    path(r'api/face/video/<str:filename>/', views.VideoDownloadViewSet)
]

