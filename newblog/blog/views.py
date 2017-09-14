from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown
from comments.forms import CommentForm


# 原先版本
# def index(request):
#     return HttpResponse("欢迎访问")
#
# # 这个视图函数index首先接受了一个名为 request 的参数，
# # 这个 request 就是 Django 为我们封装好的 HTTP 请求，它是类 HttpRequest 的一个实例。
# # 然后我们便直接返回了一个 HTTP 响应给用户，这个 HTTP 响应也是 Django 帮我们封装好的，
# # 它是类 HttpResponse 的一个实例，只是我们给它传了一个自定义的字符串参数。

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

    # all() 方法从数据库里获取了全部的文章,返回的是一个 QuerySet,类似列表结构
    # 然后依据字段create_time 逆序排列，即新发表在前
    # render 渲染了 blog\index.html 模板文件，并且把包含文章列表数据的 post_list 变量传给了模板。


# 开发流程：首先配置 URL，即把相关的 URL 和视图函数绑定在一起，
# 然后实现视图函数，编写模板并让视图函数渲染模板。

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    # 用markdown格式渲染html
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()  # 获取稳这篇文章下全部评论
    context = {'post': post,  # 将文章，表单，以及评论作为模板变量传给detail.html
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


# 归档视图函数，根据文章发表年月来过滤，create_time是python的data对象，有一个year和month属性，
# 一般用·调用，这里是作为函数的参数列表，用双下划线__代替点。
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 分类视图
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
