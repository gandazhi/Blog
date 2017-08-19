# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog, Banner


# Create your views here.


class BlogView(View):
    def get(self, request):
        blog = Blog.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(blog, 12, request=request)
        blogs = p.page(page)
        return render(request, 'blog.html', {'blogs': blogs})


class IndexView(View):
    def get(self, request):
        banners = Banner.objects.all().order_by('-add_time')
        recommend_blogs = Blog.objects.filter(is_recommend=True)
        return render(request, 'index.html', {'banners': banners, 'recommend_blogs': recommend_blogs})
