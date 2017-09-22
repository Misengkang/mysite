# -*- coding:utf-8 -*-
# !/usr/bin/env python

from django.conf.urls import url

from . import views

app_name = 'guestbook'
urlpatterns = [
    url(r'^message/$', views.message, name='message'),
]