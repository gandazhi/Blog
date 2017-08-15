# _*_ coding:utf-8 _*_ 

import xadmin

from .models import UserProfile, EmailVerifyRecord

__author__ = 'gandazhi'
__date__ = '17-8-15 下午11:13'


class UserProfileAdmin(object):
    list_display = ['nick_name', 'image', 'mobile', 'email']
    search_fields = ['nick_name', 'mobile', 'email']
    list_filter = ['add_time']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email']
    list_filter = ['send_type', 'send_time']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
