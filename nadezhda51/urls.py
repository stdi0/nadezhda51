"""nadezhda51 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from index import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^news/', views.news, name='news'),
    url(r'^albom/', views.albom, name='albom'),
    url(r'^photo/(?P<photo_folder>.+)/$', views.photo, name='photo'),
    url(r'^activities/', views.activities, name='activities'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^details/', views.details, name='details'),
    url(r'^people/', views.people, name='people'),
    url(r'^reviews/', views.reviews, name='reviews'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
