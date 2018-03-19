# -*- coding:utf-8 -*-
# !/usr/bin/env python

from django.conf.urls import url


from . import views

app_name = 'discovery'
urlpatterns = [

    url(r'^d_index/$', views.d_index, name="d_index"),
    ]
