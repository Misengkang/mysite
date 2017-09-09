from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    # 把这一部分数字以article_id作为组名去匹配，组名和响应函数中参数名必须一致
    url(r'^edit/action$', views.edit_action, name='edit_action'),

]
