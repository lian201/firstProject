"""firstDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import view, testdb, search, test

# r'^$ --> 根目录  --> http://127.0.0.1:8000
# r'^hello$  --> 根目录下hello路径  --> http://127.0.0.1:8000/hello
# r'^testdb$  --> 根目录下testdb路径  --> http://127.0.0.1:8000/testdb
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^hello', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search_form$', search.search_form),
    url(r'^search_get$', search.search_get),
    url(r'^search_post$', search.search_post),
    url(r'^test$', test.test),
    url(r'^add$', test.add),
    url(r'^find$', test.find)
]
