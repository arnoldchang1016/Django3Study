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
from django.urls import path

from myapp1.views import sayhello, hello, hello3, hello5 # added by Arnold
from myapp1.views import dice ,dice2, dice3 #, show, filter # added by Arnold

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sayhello), # added by Arnold
    path('hello/<slug:username>', hello), # added by Arnold
    path('hello3/<slug:username>', hello3), # added by Arnold
    path('hello5/<slug:username>', hello5), # added by Arnold

    path('dice/', dice), # added by Arnold
    path('dice2/', dice2), # added by Arnold
    path('dice3/', dice3), # added by Arnold
#    path('show/', show), # added by Arnold
#    path('filter/', filter), # added by Arnold
]
