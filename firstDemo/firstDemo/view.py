# -*- coding: utf-8 -*-

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!--new'
    return render(request, 'nhello.html', context)