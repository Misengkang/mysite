# -*- coding:utf-8 -*-
# !/usr/bin/env python

from ..models import Post, Category
from django import template

# 按照django的规定注册函数为模板标签
register = template.Library()


# 自定义模板标签用于获取最新文章列表
# 导入 template 模块，实例化一个 template.Library 类，
# 将函数 get_recent_posts 装饰为 register.simple_tag。
# 这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


# 自定义归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')
    # date()方法返回一个列表，元素为每一篇文章创建时间（python的date对象），精确到月份，降序排列


# 自定义文章分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
