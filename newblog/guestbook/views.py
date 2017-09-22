# -*- coding:utf-8 -*-
# !/usr/bin/env python

from .models import Message
from .forms import MessageForm
from django.shortcuts import render, get_object_or_404, redirect


def message(request):
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = MessageForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            comment.save()
            messages = Message.objects.all()
            return render(request, 'blog/message.html', context={'messages': messages})

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            messages = Message.objects.all()
            context = {
                'form': form,
                'message_list': messages
            }
            return render(request, 'blog/message.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return False

    # redirect 既可以接收一个 URL 作为参数，也可以接收一个模型的实例作为参数
    # 例如这里的 post，这个实例必须实现了 get_absolute_url 方法）
