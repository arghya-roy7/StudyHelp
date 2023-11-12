from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentLogin, name='studentLogin'),
    path('index/', views.index, name='index'),
    path('student-login/', views.studentLogin, name='studentLogin'),
    path('faculty-login/', views.facultyLogin, name='facultyLogin'),
    path('staff-login/', views.staffLogin, name='staffLogin'),
    path('student-register/', views.studentRegister, name='studentRegister'),
]