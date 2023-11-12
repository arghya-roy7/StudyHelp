from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10 ,unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    enrolled_semester = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.student_id
    
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty_initial = models.CharField(max_length=10, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    joined_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.faculty_initial

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    joined_date = models.DateField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name