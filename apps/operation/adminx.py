# _*_ coding:utf-8 _*_ 

import xadmin

from .models import UserComment

__author__ = 'gandazhi'
__date__ = '17-8-15 下午11:22'


class UserCommentAdmin(object):
    list_display = ['user', 'comment', 'blog']
    search_fields = ['user', 'blog']
    list_filter = ['add_time', 'user']


xadmin.site.register(UserComment, UserCommentAdmin)
