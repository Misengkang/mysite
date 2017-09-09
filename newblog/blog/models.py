from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# 分类表格
class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型。
    CharField 的 max_length 参数指定其最大长度，单位是字符，超过这个长度的分类名就不能被存入数据库。
    Django 提供了多种数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签表格
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章表格
class Post(models.Model):
    title = models.CharField(max_length=70)  # 标题
    body = models.TextField()  # 正文
    create_time = models.DateTimeField()  # 创建时间
    modified_time = models.DateTimeField()  # 最后一次修改时间

    # 摘要，默认 CharField 要求必须存入数据，设定 blank=True 参数值后就可以允许空值。
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)  # 关联文章和分类，多对一
    tags = models.ManyToManyField(Tag, blank=True)  # 关联文章和标签，多对多

    # 作者从django.contrib.auth.models 导入，是django 写好的用户模型 model，专门处理注册登录等
    # 这里把文章和User关联起来，多对一
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    # reverse()函数用于构造url，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，
    # 那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。
    # 此函数用于index模板返回标题文章详情页面（或者直接用URL模板标签链接）
