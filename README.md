# firstProjectlian201 's first project

## 第一个项目
### python学习路线：https://www.zhihu.com/question/29138020

### Django入门 http://www.runoob.com/django/django-tutorial.html

### Django入门 https://docs.djangoproject.com/en/1.11/intro/tutorial01/



### 创建APP
```
django-admin.py startapp TestModel
```

### 数据库表改动后刷新数据库
```
python3 manage.py makemigrations TestMySqlModel
python3 manage.py migrate TestMySqlModel
```

### 启动server
定位到包含__init__的文件夹下
```
python3 manage.py runserver
```
