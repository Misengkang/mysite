# -*- coding:utf-8 -*-
# !/usr/bin/env python
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

]


# 当用户输入网址 http://127.0.0.1:8000 后，
# Django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，
# 此时只剩下一个空字符串，而 r'^$' 的模式正是匹配一个空字符串,
# (这个正则表达式的意思是以空字符串开头且以空字符串结尾），
# 于是二者匹配，Django 便会调用其对应的 views.index 函数。

# 正则含义：r'^post/(?P<pk>[0-9]+)/$'，以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，
# 如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数
# (?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串捕获并作为关键字参数
# 传给其对应的视图函数 detail。比如当用户访问 post/255/ 时
# 被括起来的部分 (?P<pk>[0-9]+) 匹配 255，那么这个 255 会在调用视图函数
# （注意 Django 并不关心域名，而只关心去掉域名后的相对 URL）
# detail 时被传递进去，实际上视图函数的调用就是这个样子：detail(request, pk=255)。
# 我们这里必须从 URL 里捕获文章的 id，因为只有这样我们才能知道用户访问的究竟是哪篇文章。


# 归档视图archives对应的 URL 的正则表达式两个括号括起来的地方是两个命名组参数，
# Django 会从用户访问的 URL 中自动提取这两个参数的值，然后传递给其对应的视图函数。
# 例如如果用户想查看 2017 年 3 月下的全部文章，他访问 /archives/2017/3/，
# 那么 archives 视图函数的实际调用为：archives(request, year=2017, month=3)
