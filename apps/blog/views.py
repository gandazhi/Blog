# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blog


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
