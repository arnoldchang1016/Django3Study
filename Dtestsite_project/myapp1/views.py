from django.shortcuts import render

from django.http import HttpResponse # added by Arnold

from datetime import datetime

# Create your views here.

def sayhello(request): # added by Arnold
	return HttpResponse("<h1> Hello ... </h1>")

def hello(request, username): # added by Arnold
	return HttpResponse("<h1> Hello, " + username  + "</h1>")

def hello3(request, username): # added by Arnold
	now = datetime.now()
	return render(request, "hello_template.html", locals())

def hello5(request, username): # added by Arnold
	now = datetime.now()
	return render(request, "hello5_template.html", locals())