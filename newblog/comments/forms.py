# -*- coding:utf-8 -*-
# !/usr/bin/env python
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

# 正常的前端表单代码应该在html文档里写，但是我们目前并没有写这些代码，
# 而是写了一个 CommentForm 这个 Python 类。通过调用这个类的一些方法和属性，
# Django 将自动为我们创建常规的表单代码，接下来的教程我们就会看到具体是怎么做的。
