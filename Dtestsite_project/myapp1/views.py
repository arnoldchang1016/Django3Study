from django.shortcuts import render

from django.http import HttpResponse # added by Arnold

from datetime import datetime

import random

from myapp1.models import student # added by Arnold on 2020-09-17
from django.shortcuts import redirect # added by Arnold on 2020-09-26

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

times = 0 # declare global variable 

def dice3(request):
	global times
	times = times + 1
	local_times = times
	username1 = "David"
	no1 = random.randint(1, 6) # added by Arnold
	no2 = random.randint(1, 6) # added by Arnold
	no3 = random.randint(1, 6) # added by Arnold
	return render(request, "dice3.html", locals())

def filter(request):
	value = 4
	list1 = [1, 2, 3]
	pw = '芝麻開門'

	html = '<h3> Hello </h3>'
	value2 = True
	return render(request, 'filter.html', locals())

def listone(request): #added by Arnold on 2020-09-17
	try:
		unit = student.objects.get(cName='JessieCheng')
	except:
		errormessage = '讀取錯誤'

	return render(request, "listone.html", locals())

def listall(request): #added by Arnold on 2020-09-17
	try:
		students = student.objects.all().order_by('id')
	except:
		errormessage = '讀取錯誤'
	
	return render(request, "listall.html", locals())

def index(request): #added by Arnold on 2020-09-17
	try:
		students = student.objects.all().order_by('cName')
	except:
		errormessage = '讀取錯誤'
	
	return render(request, "index.html", locals())

def post(request): # added by Arnold on 2020-09-26
	if request.method == 'POST':
		mess = request.POST['username']
	else:
		mess = '標單資料尚未送出!!!'

	return render(request, "post.html", locals())

def post1(request): # added by Arnold on 2020-09-26
	if request.method == "POST":
		cName = request.POST['cName']
		cSex = request.POST['cSex']
		cBirthday = request.POST['cBirthday']
		cEmail = request.POST['cEmail']
		cPhone = request.POST['cPhone']
		cAddr = request.POST['cAddr']
		unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
		unit.save() # write into database
		return redirect('/index/')
	else:
		message = '請輸入資料 (資料不做驗證)'

	return render(request, "post1.html", locals())