from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^under_maintain/$', views.under_maintain, name='under_maintain'),
]

#try
# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, url
#from . import views

#urlpatterns = patterns('blog.views',
#    url(r'^list/$', views.list, name='list'),
#)
#end try
