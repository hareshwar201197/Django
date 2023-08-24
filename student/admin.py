from django.contrib import admin

from student.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Student._meta.fields]

admin.site.register(Student, StudentAdmin)

