# Django

## Django is Python Web development framework.

## Django is built for Python 3.x -> Built for the latest version of Python

## Batteries included -> Offers built-in solutions and features for basically all problems -> is customisable & extensible

## Build Production-ready Websites -> Django can be used and is used for building real websites.




1. Setup & Understanding Django
2. URLs, Routes & Views
3. Templates & Static files
4. Data, Models & Relationships

1. Working with Forms
2. Class-based Views
3. File Uploads
4. Sessions


install django

python3 -m pip install Django

try `django-admin` to verify whether django was installed correctly.

Craete a django project:

`django-admin startproject myproject`

install `autopep8`(code format), `pylance`(code checks & completion) extension in VSCode.
enable `pylance` in your project in your `.vscode/settings.json` file:
```json
{
    "python.languageServer": "Pylance"
}
```

analyse initial django python files:
`manage.py`: run project speicific command
`__init__.py`: identify this project is a python module.
`asgi.py` & `wsgi.py`: deploy or finish our project to a real server, you need to change something in these files.
`settings.py`: configure lots of behaviours of a django project.
`urls.py`: start adding more and more pages for our django project.

start a development server: run `manage.py` with a subcommand supported by `manage.py`

`python3 manage.py runserver`

`module` in django called `app`. Apps are building blocks for the overall project. Hence `App` ~= `Module`

`python3 manage.py startapp challenges`
Analyse initial django app python files:
`migrations` folder
`__init__.py`
`admin.py`
`apps.py`
`models.py`
`tests.py`
`views.py`

URLs/Routes: URL-Action mappings which ensure that certain results are "achieved" when certain URLs are entered by the user.

What are "Views"?
The logic that is exectued for different URLs(and Http methods)
In Django, it normally is a Function or a Class, which is the code that handles requests and returns responses. 

如何定义新的Views和URLs？

1. 在各自的APP下面建立urls.py文件，在其中定义路由和对应的View Function，如：
```python
from django.urls import path
from . import views

# List all urls we want to support
urlpatterns = [
    # path("challenges/") # No need with the prefix "challenges"
    path("january", view=views.index)
]
```
2. 如果需要创建动态路由，则需要使用`<>`语法来描述route：

```python
from django.urls import path
from . import views

# List all urls we want to support
urlpatterns = [
    # path("challenges/") # No need with the prefix "challenges"
    path("january", view=views.january),
    path("februray", view=views.february),
    path("<month>", view=views.monthly_challenge)
]

```
在入口的Functions中，需要如下定义：1232
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# define a python function for a view.
def january(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("This works for FEB!")

def monthly_challenge(request, month):
    return HttpResponse()
```
3. 可以根据路由类型的不同，动态调整路由的优先级：

```python

```

4. 重定向路由到另一个View中。使用HttpResponseRedirect，并且通过reverse构造URL


nitty-grittysdqw
