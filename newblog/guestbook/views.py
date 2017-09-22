# -*- coding:utf-8 -*-
# !/usr/bin/env python

from .models import Message
from django.shortcuts import render, get_object_or_404, redirect


def message(request):
    messages = Message.objects.all()
    return render(request, 'blog/message.html', context={'messages': messages})
