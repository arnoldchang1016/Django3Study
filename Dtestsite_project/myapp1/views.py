from django.shortcuts import render

from django.http import HttpResponse # added by Arnold

from datetime import datetime

import random

from myapp1.models import student # added by Arnold on 2020-09-17
from django.shortcuts import redirect # added by Arnold on 2020-09-26
from myapp1.form import PostForm # added by Arnold on 2020-09-27 

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

def postform(request): #added by Arnold on 2020-09-27
	# postform = PostForm(request.POST)
	postform = PostForm()
	return render(request, 'postform.html', locals())

def post2(request): # added by Arnold on 2020-09-29
	if request.method == "POST":
		postform = PostForm(request.POST) # 建立form物件
		if postform.is_valid():
			cName = postform.cleaned_data['cName']
			cSex = postform.cleaned_data['cSex']
			cBirthday = postform.cleaned_data['cBirthday']
			cEmail = postform.cleaned_data['cEmail']
			cPhone = postform.cleaned_data['cPhone']
			cAddr = postform.cleaned_data['cAddr']
			unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
			unit.save() # write into database
			message = '已儲存...'
			return redirect('/index/')
		else: 
			message = '驗證碼錯誤'
	else:
		message = '姓名、性別、生日必須輸入!'
		postform = PostForm()
	return render(request, "post2.html", locals())

def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			unit = student.objects.get(id=id)  
			unit.delete()	
			return redirect('/index/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	

def edit(request, id=None, mode=None): # added by Arnold on 2020-10-03
	if mode == "edit": # coming from the submit of edit.html
		unit = student.objects.get(id=id)
		unit.cName = request.GET['cName']
		unit.cSex = request.GET['cSex']
		unit.cBirthday = request.GET['cBirthday']
		unit.cEmail = request.GET['cEmail']
		unit.cPhone = request.GET['cPhone']
		unit.cAddr = request.GET['cAddr']
		unit.save() # write into database
		message = '已修改...'
		return redirect('/index/')
	else: # coming from URL
		try: 
			unit = student.objects.get(id=id)
			strdate = str(unit.cBirthday)
			strdate2 = strdate.replace('年','-')
			strdate2 = strdate.replace('月','-')
			strdate2 = strdate.replace('日','-')
			unit.cBirthday = strdate2
		except:
			message = '此 id 不存在！'
	return render(request, "edit.html", locals())

def edit2(request, id=None, mode=None): # added by Arnold on 2020-10-03
	if mode == "load": # coming from the 編輯二 of index.html
		unit = student.objects.get(id=id)
		strdate = str(unit.cBirthday)
		strdate2 = strdate.replace('年','-')
		strdate2 = strdate.replace('月','-')
		strdate2 = strdate.replace('日','-')
		unit.cBirthday = strdate2
		return render(request, "edit2.html", locals())

	elif mode == "save" : # coming from edit2.html
		unit = student.objects.get(id=id)
		unit.cName = request.POST['cName']
		unit.cSex = request.POST['cSex']
		unit.cBirthday = request.POST['cBirthday']
		unit.cEmail = request.POST['cEmail']
		unit.cPhone = request.POST['cPhone']
		unit.cAddr = request.POST['cAddr']
		unit.save() # write into database
		message = '已修改...'
		return redirect('/index/')		