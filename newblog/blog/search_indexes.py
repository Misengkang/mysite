# -*- coding:utf-8 -*-
# !/usr/bin/env python

from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True，这代表 django haystack 和搜索引擎将使用此字段的内容作为索引进行
    # 检索(primary field),一个字段设置了document=True，则一般约定此字段名为text,
    # use_template=True允许我们使用数据模板去建立搜索引擎索引的文件
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
