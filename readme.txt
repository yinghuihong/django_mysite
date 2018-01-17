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

==> 四、VIEW and 模板
使用命名空间存放模板，避免多个应用存在相同模板名的情况下，无法区分
Django will choose the first template it finds whose name matches, and if you had a template with the same name in a
different application, Django would be unable to distinguish between them.

---- Removing hardcoded URLs in templates
{% url 'detail' question.id%} 会采用polls/urls.py中定义的名为detail的path，当url路径更改时，不用修改模板

---- Namespacing URL names
当同一工程下存在多个app，且都有名称为detail的path，则需通过命名空间作区分
1.在polls/urls.py中添加app_name = 'polls'
2.{% url 'detail' question.id%}改为{% url 'polls:detail' question.id%}

==> 五、forms and generic views
FORM HttpResponseRedirect reverse

---- Use generic views: Less code is better
1.Convert the URLconf.
2.Delete some of the old, unneeded views.
3.Introduce new views based on Django’s generic views.

The DetailView generic view expects the primary key value captured from the URL to be called "pk",
so we’ve changed question_id to pk for the generic views.

==> 六、Tests (methods or views)
$ python manage.py test polls # running tests

What happened is this:

1.python manage.py test polls looked for tests in the polls application # 运行测试
2.it found a subclass of the django.test.TestCase class # 查找集成TestCase的子类
3.it created a special database for the purpose of testing # 测试时，会创建特殊的数据库
4.it looked for test methods - ones whose names begin with test # 查找test开头的函数
5.in test_was_published_recently_with_future_question it created a Question instance whose pub_date field is 30 days in the future # 创建Question实例
6.… and using the assertIs() method, it discovered that its was_published_recently() returns True, though we wanted it to return False # 通过断言函数做判断


==> 七、static files management

