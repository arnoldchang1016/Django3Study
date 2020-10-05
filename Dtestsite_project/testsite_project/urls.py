"""testsite_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include # added by Arnold on 2020-10-05

from myapp1.views import sayhello, hello, hello3, hello5 # added by Arnold
from myapp1.views import dice ,dice2, dice3, filter #, show, filter # added by Arnold
from myapp1.views import listone, listall, index # added by Arnold 2020-09-17
from myapp1.views import post, post1 # added by Arnold on 2020-09-26
from myapp1.views import postform # added by Arnold on 2020-09-27
from myapp1.views import post2, delete # added by Arnold on 2020-09-29
from myapp1.views import edit, edit2 # added by Arnold on 2020-10-03
from myapp1.views import login, logout # added by Arnold on 2020-10-04

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sayhello), # added by Arnold
    path('hello/<slug:username>', hello), # added by Arnold
    path('hello3/<slug:username>', hello3), # added by Arnold
    path('hello5/<slug:username>', hello5), # added by Arnold

    path('dice/', dice), # added by Arnold
    path('dice2/', dice2), # added by Arnold
    path('dice3/', dice3), # added by Arnold
    path('filter/', filter), # added by Arnold 2020-09-17
    path('listone/', listone), # added by Arnold 2020-09-17
    path('listall/', listall), # added by Arnold 2020-09-17
    path('index/', index), # added by Arnold 2020-09-17
    path('post/', post), # added by Arnold on 2020-09-26
    path('post1/', post1), # added by Arnold on 2020-09-26
    path('postform/', postform), # added by Arnold on 2020-09-27
    path('post2/', post2), # added by Arnold on 2020-09-29
    path('delete/', delete), # added by Arnold on 2020-09-29
    re_path(r'delete/(\d+)/$',delete),
    path('edit/', edit), # added by Arnold on 2020-10-03
    re_path(r'edit/(\d+)/$', edit), # added by Arnold on 2020-10-03
    re_path(r'edit/(\d+)/(\w+)$', edit), # added by Arnold on 2020-10-03
    re_path(r'edit2/(\d+)/(\w+)$', edit2), # added by Arnold on 2020-10-03
    path('login/', login), # added by Arnold on 2020-10-04
    path('logout/', login), # added by Arnold on 2020-10-04
    path('captcha/', include('captcha.urls')), # added by Arnold on 2020-10-05
]
