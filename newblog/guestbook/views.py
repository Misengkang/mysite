# -*- coding:utf-8 -*-
# !/usr/bin/env python

from .models import Message
from django.shortcuts import render
from django.http import HttpResponseRedirect


def message(request):
    messages = Message.objects.all()
    return render(request, 'blog/message.html', {'messages': messages})


def save(request):
    visitor_name = request.POST.get("visitor_name")
    visitor_email = request.POST.get("visitor_email")
    visitor_url = request.POST.get("visitor_url")
    message_text = request.POST.get("message_text")
    message = Message(visitor_name=visitor_name, visitor_email=visitor_email,
                      visitor_url=visitor_url, message_text=message_text)
    message.save()

    return HttpResponseRedirect('/message/')
