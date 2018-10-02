"""benga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from profiling import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('upload/', views.UploadBatchList.as_view(), name="upload-list"),
    path('upload/<uuid:pk>/', views.UploadBatchDetail.as_view(), name="upload-detail"),
    path('sequence/', views.SequenceList.as_view(), name="sequence-list"),
    path('sequence/<uuid:pk>/', views.SequenceDetail.as_view(), name="upload-detail"),
    path('profile/', views.ProfileList.as_view(), name="profile-list"),
    path('profile/<uuid:pk>/', views.ProfileDetail.as_view(), name="upload-detail"),
    path('dendrogram/', views.DendrogramList.as_view(), name="dendrogram-list"),
    path('dendrogram/<uuid:pk>/', views.DendrogramDetail.as_view(), name="upload-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)