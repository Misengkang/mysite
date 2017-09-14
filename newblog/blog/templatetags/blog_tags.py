# -*- coding:utf-8 -*-
# !/usr/bin/env python

from ..models import Post, Category
from django import template
from django.db.models.aggregates import Count

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
    # return Category.objects.all()
    # Category.objects.annotate方法和Category.objects.all有点类似，它会返回数据库中全部
    # Category的记录，但同时它还会做一些额外的事情，就是去统计返回的 Category
    # 记录的集合中每条记录下的文章数。代码中的 Count 方法为我们做了这个事，它接收一个和Category
    # 相关联的模型参数名（这里是 Post，通过 ForeignKey 关联的），然后它便会统计
    # Category记录的集合中每条记录下的与之关联的 Post记录的行数，也就是文章数，最后把这个值保存到
    # "num_posts属性"中。此外，我们还对结果集做了一个过滤，使用filter 方法把
    # num_posts的值小于1的分类过滤掉。因为num_posts的值小于1
    # 表示该分类下没有文章，没有文章的分类我们不希望它在页面中显示。
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)