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