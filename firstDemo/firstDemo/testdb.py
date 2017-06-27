# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestMySqlModel.models import Test


# 数据库操作
def testdb(request):
    # test1 = Test(kname="zhe",kage = "10")
    # test1.save()

    response = ""
    response1 = ""
    list = Test.objects.all()
    for var in list:
        response1 += var.kname + " "
    response = response1

    return HttpResponse("<p>" + response + "</p>")
