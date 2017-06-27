# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.shortcuts import render
from TestMySqlModel.models import Test


def test(request):
    return render_to_response("test.html")


def add(request):
    ctx = {}
    name = ""
    age = ""
    if request.POST:
        name = request.POST['q']
        age = request.POST['a']
        ctx['rlt'] = request.POST['q'] + request.POST['a']
    test = Test(kname=name, kage=age)
    test.save()
    return render(request, "test.html", ctx)


def find(request):
    ctx = {}
    value = ""
    if request.POST:
        name = request.POST['q']
        response = Test.objects.filter(kname=name)
        for var in response:
            value += var.kname + ":" + var.kage + "--"
        ctx['abc'] = value
    return render(request, "test.html", ctx)
