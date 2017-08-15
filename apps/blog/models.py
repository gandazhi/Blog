# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import models

# Create your models here.


class Blog(models.Model):
    image = models.ImageField(upload_to='image/%Y/%m', max_length=50, verbose_name=u'文章图片')
    title = models.CharField(max_length=20, verbose_name=u'文章title')
    content = models.TextField(verbose_name=u'blog文章内容')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否banner')
    is_recommend = models.BooleanField(default=False, verbose_name=u'是否推荐文章')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u'修改时间')
    desc = models.CharField(max_length=50, verbose_name=u'blog描述', default='')

    class Meta:
        verbose_name = u'Blog'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=50, verbose_name=u'banner图片')
    title = models.CharField(max_length=50, verbose_name=u'banner_title')
    desc = models.CharField(max_length=30, verbose_name=u'banner描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u'修改时间')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')

    class Meta:
        verbose_name = u'Banner'
        verbose_name_plural = verbose_name

