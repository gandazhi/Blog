# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import models

from users.models import UserProfile
from blog.models import Blog


# Create your models here.


class UserComment(models.Model):
    comment = models.CharField(max_length=100, verbose_name=u'用户评论')
    user = models.ForeignKey(UserProfile, verbose_name=u'评论用户')
    blog = models.ForeignKey(Blog, verbose_name=u'评论博客文章')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'评论时间')

    class Meta:
        verbose_name = u'用户评论'
        verbose_name_plural = verbose_name
