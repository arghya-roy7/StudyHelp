from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Student, Staff, Faculty, Announcement, Complain
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
            return redirect(studentProfile)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('studentLogin')
    return render(request, 'student_login.html')


def facultyLogin(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None and Faculty.objects.filter(user=user).exists():
            auth.login(request, user)
            # return redirect('facultyProfile')
            return HttpResponse("Faculty")
        else:
            messages.info(request, 'Invalid Credentials')
            # return redirect('facultyLogin')
            # return HttpResponse("Faculty")
    return render(request, 'faculty_login.html')

def staffLogin(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None and Staff.objects.filter(user=user).exists():
            auth.login(request, user)
            return redirect('staffProfile')
            #return HttpResponse("staff")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('staffLogin')

    return render(request, 'staff_login.html')

def studentRegister(request):
    if request.method == 'POST':
        student_id = request.POST['studentid']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=student_id).exists():
                messages.info(request, 'Username Taken')
                return redirect('studentRegister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('studentRegister')
            else:
                user = User.objects.create_user(username=student_id, email=email, password=password)
                user.save()

                student = Student.objects.create(user=user, student_id=student_id, email=email)
                student.save()
                return redirect('studentLogin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('studentRegister')  
    return render(request, 'student_reg.html')




#========================================================================= profiles
@login_required(login_url='studentLogin')
def studentProfile(request):
    if Student.objects.filter(user=request.user).exists():
        user = request.user
        obj = User.objects.get(username=user)

        if Student.objects.filter(user=obj).exists():
            obj = Student.objects.get(user=obj)
            return render(request, 'student_profile.html', {'user': obj, "student": "student"})
        
        return render(request, 'student_profile.html', {'user': obj})
    else:
        return redirect('studentLogin')
    

@login_required(login_url='staffLogin')
def staffProfile(request):
    if Staff.objects.filter(user=request.user).exists():
        user = request.user
        obj = User.objects.get(username=user)
        if Staff.objects.filter(user=obj).exists():
            obj = Staff.objects.get(user=obj)
            return render(request, 'staff_profile.html', {'user': obj, "staff": "staff"})
        return render(request, 'staff_profile.html', {'user': obj})
    else:
        return redirect('staffLogin')
    
###########################################################################################


@login_required(login_url='studentLogin')
def studentAnnouncementView(request):
    if Student.objects.filter(user=request.user).exists():
        obj = Announcement.objects.all()
        return render(request, 'student_announcement_view.html', {'obj': obj[::-1]})
    else:
        return redirect('studentLogin')
    
@login_required(login_url='staffLogin')
def staffAnnouncementView(request):
    if Staff.objects.filter(user=request.user).exists():
        obj = Announcement.objects.all()
        if request.method == 'POST':
            announcement_id = request.POST['aid']
            announcement = Announcement.objects.get(anumber = announcement_id)
            announcement.delete()

        return render(request, 'staff_announcement_view.html', {'obj': obj[::-1]})
    else:
        return redirect('staffLogin')
    


@login_required(login_url='staffLogin')
def postAnnouncement(request):
    if Staff.objects.filter(user=request.user).exists():
        cuser = Staff.objects.get(user=request.user)
        if request.method == 'POST':
            subject = request.POST['subject']
            source = request.POST['source']
            statement = request.POST['statement']
            announcement = Announcement.objects.create(subject=subject, source=source, statement=statement, datetime = datetime.now(), posted_by=cuser)
            announcement.save()
            return redirect('staffAnnouncementView')
        return render(request, 'post_announcement.html')
    else:
        return redirect('staffLogin')
    



















@login_required(login_url='studentLogin')
def complainStudentView(request):
    if Student.objects.filter(user=request.user).exists():
        user = request.user
        complain = Complain.objects.all()
        # n_complain = []
        # for c in complain:
        #     if c.posted_by == user:
        #         n_complain.append(c)
        # context = {
        #     'complain': n_complain[::-1]
        # }
        context = {
            'complain': complain[::-1]
        }
        return render(request, 'complain_student_view.html', context)
    else:
        return redirect('studentLogin')
    

@login_required(login_url='staffLogin')
def complainStaffView(request):
    if Staff.objects.filter(user=request.user).exists():
        cuser = Staff.objects.get(user=request.user)
        complain = Complain.objects.all()
        context = {
            'complain': complain[::-1]
        }
        if request.method == 'POST' and request.POST['status'] == 'resolved':
            cnum = request.POST['cnum']
            status = "resolved"
            resolved_by = cuser

            complain = Complain.objects.get(cnumber=cnum)
            complain.status = status
            complain.resolved_by = resolved_by
            complain.save()
            return redirect('complainStaffView')
        elif request.method == 'POST' and request.POST['status'] == 'rejected':
            cnum = request.POST['cnum']
            status = "rejected"
            resolved_by = cuser

            complain = Complain.objects.get(cnumber=cnum)
            complain.status = status
            complain.resolved_by = resolved_by
            complain.save()
            return redirect('complainStaffView')
        return render(request, 'complain_staff_view.html', context)
    else:
        return redirect('staffLogin')
    



@login_required(login_url='studentLogin')
def postComplain(request):
    if Student.objects.filter(user=request.user).exists():
        cuser = Student.objects.get(user=request.user)
        if request.method == 'POST':
            tag = request.POST['tag']
            statement = request.POST['statement']

            complain = Complain.objects.create(tag=tag, statement=statement, datetime = datetime.now(), posted_by=cuser)
            complain.save()
            return redirect('complainStudentView')
        return render(request, 'post_complain.html')
    else:
        return redirect('studentLogin')

