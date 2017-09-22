# -*- coding:utf-8 -*-
# !/usr/bin/env python
from django import forms
from .models import Message


class MessageForm(forms.ModelForm):  # Django 的表单类必须继承自 forms.Form 类或者 forms.ModelForm 类
    class Meta:  # 指定表单相关东西，Meta是一个内部类，它用于定义一些Django模型类的行为特性
        model = Message  # 指定表单对应数据库模型
        fields = ['visitor_name', 'visitor_email', 'message_text']  # 指定表单显示字段