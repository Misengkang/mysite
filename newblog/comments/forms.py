# -*- coding:utf-8 -*-
# !/usr/bin/env python
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):  # Django 的表单类必须继承自 forms.Form 类或者 forms.ModelForm 类
    class Meta:  # 指定表单相关东西，Meta是一个内部类，它用于定义一些Django模型类的行为特性
        model = Comment  # 指定表单对应数据库模型
        fields = ['name', 'email', 'text']  # 指定表单显示字段

# 正常的前端表单代码应该在html文档里写，但是我们目前并没有写这些代码，
# 而是写了一个 CommentForm 这个 Python 类。通过调用这个类的一些方法和属性，
# Django 将自动为我们创建常规的表单代码，接下来的教程我们就会看到具体是怎么做的。
