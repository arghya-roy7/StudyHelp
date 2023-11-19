from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentLogin, name='studentLogin'),
    path('index/', views.index, name='index'),
    path('student-login/', views.studentLogin, name='studentLogin'),
    path('faculty-login/', views.facultyLogin, name='facultyLogin'),
    path('staff-login/', views.staffLogin, name='staffLogin'),
    path('student-register/', views.studentRegister, name='studentRegister'),
    path('student-profile/', views.studentProfile, name='studentProfile'),
    path('staff-profile/', views.staffProfile, name='staffProfile'),

    path('student-announcement-view/', views.studentAnnouncementView, name='studentAnnouncementView'),
    path('staff-announcement-view/', views.staffAnnouncementView, name='staffAnnouncementView'),
    path('post-announcement/', views.postAnnouncement, name='postAnnouncement'),

    path('complain-student-view/', views.complainStudentView, name='complainStudentView'),
    path('complain-staff-view/', views.complainStaffView, name='complainStaffView'),
    path('post-complain/', views.postComplain, name='postComplain'),
]