from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=128, blank=False, verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='修改日期', default=datetime.now)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    article_views = models.PositiveIntegerField(default=0, verbose_name='文章访问量')

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, blank=False, verbose_name='评论内容')
    commentator = models.ForeignKey(User, verbose_name='评论人', on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)

    class Meta:
        ordering = ['-created_date']
