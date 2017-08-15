# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.


class UserProfile(models.Model):
    nick_name = models.CharField(max_length=10, verbose_name=u'昵称', default='')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    image = models.ImageField(upload_to='photo/%Y/%m', max_length=100, verbose_name=u'用户头像')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'注册时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=6, verbose_name=u'邮箱验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'忘记密码')), verbose_name=u'验证码类型',
                                 max_length=6)
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name
