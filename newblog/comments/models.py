from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    # auto_now_add 的作用是，当评论数据保存到数据库时，自动把 create_time 的值指定为当前时间。
    create_time = models.DateTimeField(auto_now_add=True)
    # 关联文章和评论，一对多
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
