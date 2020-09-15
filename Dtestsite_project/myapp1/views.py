from django.shortcuts import render

from django.http import HttpResponse # added by Arnold

from datetime import datetime

import random

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

def dice(request):
	no = random.randint(1, 6) # added by Arnold
	return render(request, "dice.html", locals())
#	return render(request, "dice.html", {"no":no})

def dice2(request):
	no1 = random.randint(1, 6) # added by Arnold
	no2 = random.randint(1, 6) # added by Arnold
	no3 = random.randint(1, 6) # added by Arnold
	return render(request, "dice2.html", locals())


def dice3(request):
	times = times + 1
    # local_times = times
    username = 'David'
	no1 = random.randint(1, 6) # added by Arnold
	no2 = random.randint(1, 6) # added by Arnold
	no3 = random.randint(1, 6) # added by Arnold
	return render(request, "dice3.html", locals())


global times # declare global variable 
times = 0