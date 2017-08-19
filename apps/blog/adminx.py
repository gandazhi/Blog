# _*_ coding:utf-8 _*_ 

import xadmin

from .models import Blog, Banner

__author__ = 'gandazhi'
__date__ = '17-8-15 下午10:53'


class BlogAdmin(object):
    list_display = ['image', 'title', 'desc', 'content', 'is_banner', 'is_recommend', 'click_num']
    search_fields = ['title', 'desc']
    list_filter = ['add_time', 'update_time', 'is_banner', 'is_recommend']
    readonly_fields = ['click_num', 'add_time', 'update_time']
    style_fields = {'content': 'ueditor'}


class BannerAdmin(object):
    list_display = ['image', 'title', 'desc', 'click_num']
    search_fields = ['title', 'desc']
    list_filter = ['add_time', 'update_time']
    readonly_fields = ['click_num', 'add_time', 'update_time']

xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Banner, BannerAdmin)
