# -*- coding:utf-8 -*-
# !/usr/bin/env python
from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),原先版本
    url(r'^$', views.IndexView.as_view(), name='index'),  # 调用类视图的as_view（）方法使类视图转换函数视图
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),原先版本
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),原先版本
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # url(r'^search/$', views.search, name='search') 原先搜索视图
    url(r'^about/$', views.about, name='about'),
    url(r'^todo/$', views.todo, name='todo'),

]

# 每一个 URL 对应着一个视图函数，这样当用户访问这个 URL 时，
# Django 就知道调用哪个视图函数去处理这个请求了。
# 在 Django 中 URL 模式的配置方式就是通过 url 函数将 URL 和视图函数绑定。
# 比如 url(r'^$', views.index, name='index')，它的第一个参数是 URL 模式，
# 第二个参数是视图函数 index。对 url 函数来说，第二个参数传入的值必须是一个函数


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
