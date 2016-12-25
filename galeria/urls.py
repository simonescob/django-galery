"""galeria URL Configuration

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
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import *
from django.conf.urls.static import static

from accounts.views import login_view, logout_view, register_view, index, edit_view

urlpatterns = [
	url(r'^$', index, name="user-home"),
	url(r'^edit/$', edit_view, name="user-edit"),
	url(r'^login/$', login_view, name='login'),
	url(r'^logout/$', logout_view, name='logout'),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^register/$', register_view, name='register'),
	url(r'^fotos/(?P<user_id>[\w]+)/', include('fotos.urls')),
	url(r'^administrator/', admin.site.urls, name="admin"),
	url(r'^noti/', include('noti.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



