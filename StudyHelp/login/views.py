from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def studentLogin(request):
    if request.method == 'POST':
        student_id = request.POST['studentid']
        password = request.POST['password']

        user = auth.authenticate(username=student_id, password=password)

        if user is not None and Student.objects.filter(student_id=student_id).exists():
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('studentLogin')
    return render(request, 'student_login.html')
