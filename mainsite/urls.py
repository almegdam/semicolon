"""mainsite URL Configuration

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
#from django.conf.urls import include, url
from django.contrib import admin
#try
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
#    (r'^', include('blog.urls')),
#)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#end try with comments after
urlpatterns = [
    url(r'^admin/', admin.site.urls),
		url(r'', include('blog.urls')),
#		url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#		url(r'^login/$', 'blog.views.login_user'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
