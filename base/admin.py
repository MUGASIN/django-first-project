from django.contrib import admin
from base.models import student,Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','desg','sal','gender']

admin.site.register(student)
admin.site.register(Employee,EmployeeAdmin)