# firstProjectlian201 's first project

## 第一个项目
### python学习路线：https://www.zhihu.com/question/29138020

### Django入门 http://www.runoob.com/django/django-tutorial.html

### Django入门 https://docs.djangoproject.com/en/1.11/intro/tutorial01/



# Python3中没有mysqldb，使用pymysql替代mysqldb

> 参考：http://blog.csdn.net/it_dream_er/article/details/52093362

需要在项目mysite/mysite/\_\_init__.py中添加以下配置
```
import pymysql
pymysql.install_as_MySQLdb()
```

# Demo

### 1.创建项目
```
django-admin.py startproject mysite
```
### 2.创建APP
```
django-admin.py startapp weblog
```
### 3.使用mysql创建数据库
- root权限登录mysql
    > mysql -uroot -p
- 新建用户
    > CREATE USER 'zhe'@'localhost' IDENTIFIED BY '1234';
- 创建数据库
    > create database weblog default character set utf8;
- 将数据库分配给用户
    > grant all privileges on weblog.* to zhe@localhost identified by '1234';
- 刷新
    > flush privileges

### 4.添加应用
将新建的app添加到mysite/mysite/settings.py中的INSTALLED_APPS下
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weblog',
)
```
### 5.添加数据库字段
在weblog下的models中添加数据类并注册进django
```
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publish_date = models.DateTimeField()

admin.site.register(Post)
```
### 6.数据库
创建表结构
```
python3 manage.py migrate
```
数据库表改动后刷新数据库
```
python3 manage.py makemigrations weblog
python3 manage.py migrate weblog
```

### 7.启动server
```
python3 manage.py runserver
```

### 8.创建后台超级用户
```
python3 manage.py createsuperuser
```

### 9.访问后台应用,使用刚才创建的用户登录
> http://127.0.0.1:8000/admin
