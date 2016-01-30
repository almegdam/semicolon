from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^under_maintain/$', views.under_maintain, name='under_maintain'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^login/$', views.login_user, name="login"),	
]

#try
# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, url
#from . import views

#urlpatterns = patterns('blog.views',
#    url(r'^list/$', views.list, name='list'),
#)
#end try
