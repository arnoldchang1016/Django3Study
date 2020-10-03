from django import forms

class PostForm(forms.Form):
	cName = forms.CharField(max_length=20, initial='')
	cSex = forms.CharField(max_length=2, initial='M')
	cBirthday = forms.DateField()
	cEmail = forms.EmailField(max_length=100, initial='', required=False)
	cPhone = forms.CharField(max_length=50, initial='', required=False)
	cAddr = forms.CharField(max_length=255, initial='', required=False)

postform = PostForm()

cName = 'David'
cSex = 'M'
cBirthday = ''
cEmail = ''
cPhone = ''
cAddr = ''

postform = PostForm({'cName':cName, 'cSex':cSex, 'cBirthday':cBirthday, 'cEmail':cEmail, 'cPhone':cPhone, 'cAddr':cAddr})
# postform = PostForm(request.POST)