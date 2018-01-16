==> 一、Install
$ pip install django //安装django
$ python -m django --version //检查django是否安装成功

==> 二、Project apps and web server
$ django-admin startproject mysite //创建工程
$ python manage.py runserver //运行服务，django内置轻量的Web服务器（纯python编写），仅用于开发测试时使用
$ python manage.py startapp polls //创建app
1、write view
2、write app URL config
3、project URL include app URL

==> 三、Database setup
SQLite is included in Python, so you won’t need to install anything else to support your database.
If you’re using SQLite, you don’t need to create anything beforehand - the database file will be created automatically when it is needed.

---- 1.INSTALLED_APPS
Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.
django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.

$ python manage.py migrate //为INSTALLED_APPS的应用创建表
不需要的应用则从INSTALLED_APPS中注释或删掉，然后才执行migrate命令
The migrate command will only run migrations for apps in INSTALLED_APPS.

---- 2.Creating models
The goal is to define your data model in one place and automatically derive things from it.

---- 3.Activating models
But first we need to tell our project that the polls app is installed.
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
    ]
$ python manage.py makemigrations polls //创建表迁移描述文件（polls/migrations目录下）
$ python manage.py migrate //执行迁移，真正修改数据库

$ python manage.py sqlmigrate polls 0001 //展示django执行的SQL语句（只展示不执行，便于理解django的操作）
$ python manage.py check

表模型修改三步骤：
1.Change your models (in models.py).
2.Run python manage.py makemigrations to create migrations for those changes
3.Run python manage.py migrate to apply those changes to the database.

---- 4.Playing with the API
$ python manage.py shell
https://docs.djangoproject.com/en/2.0/intro/tutorial02/#playing-with-the-api

---- 5.Introducing the Django Admin
Creating an admin user
$ python manage.py createsuperuser
Username: admin
Password: yinghuihong

---- 6.Start the development server
$ python manage.py runserver

---- 7.Make the poll app modifiable in the admin
from django.contrib import admin
from .models import Question
admin.site.register(Question)




