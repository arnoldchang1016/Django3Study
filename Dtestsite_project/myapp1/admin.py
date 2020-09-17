from django.contrib import admin

# Register your models here.

from myapp1.models import student

# first approach added by Arnold 2020-09-17
# admin.site.register(student)

# second approach added by Arnold 2020-09-17
class studentAdmin(admin.ModelAdmin):
	list_display=('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
	list_filter=('cName', 'cSex')
	search_fields=('cName',)
	ordering=('id',)


admin.site.register(student, studentAdmin)