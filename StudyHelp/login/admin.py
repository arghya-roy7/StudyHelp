from django.contrib import admin
from .models import Student, Staff, Faculty

# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Faculty)
