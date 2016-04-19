#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
from blog import views

urlpatterns = [
    url(r'^list/$', views.blog_list, name='bloglist'),
    url(r'^(\d+)/$', views.blog_show, name='detailblog'),
    url(r'^add/$', views.blog_add, name='addblog'),
    url(r'^(\d+)/update/$', views.blog_update, name='updateblog'),
    url(r'^(\d+)/del/$', views.blog_del, name='delblog'),
    url(r'^tag/(\d+)/$', views.blog_filter, name='filtrblog'),
    url(r'^(?P<id>\d+)/commentshow/$', views.blog_show_comment, name='showcomment'),

    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
]

# urlpatterns = patterns(('blog.views'),
#     url(r'^list/$', 'blog_list', name='bloglist'),
#     url(r'^(?P<id>\d+)/$', 'blog_show', name='detailblog'),
#     url(r'^add/$', 'blog_add', name='addblog'),
#     url(r'^(?P<id>\w+)/update/$', 'blog_update', name='updateblog'),
#     url(r'^(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
#     url(r'^tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
#
#     # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
# )
