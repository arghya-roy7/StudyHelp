from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentLogin, name='studentLogin'),
    path('index/', views.index, name='index'),
    path('student-login/', views.studentLogin, name='studentLogin'),
    path('student-logout/', views.student_logout, name="student_logout"),
    path('faculty-login/', views.facultyLogin, name='facultyLogin'),
    path('staff-login/', views.staffLogin, name='staffLogin'),
    path('staff-logout/', views.staff_logout, name="staff_logout"),
    path('student-register/', views.studentRegister, name='studentRegister'),
    path('student-profile/', views.studentProfile, name='studentProfile'),
    path('faculty-profile/', views.faculty_profile, name='faculty_profile'),
    path('staff-profile/', views.staffProfile, name='staffProfile'),
    path('faculty-see-courses', views.see_course_list, name='faculty_see_courses'),
    path('faculty-delete-course/<int:id>',
         views.delete_course, name="faculty_delete_course"),
    path('faculty-make-announcement', views.faculty_course_announcement,
         name="faculty_make_announcement"),

    path('student-announcement-view/', views.studentAnnouncementView,
         name='studentAnnouncementView'),
    path('staff-announcement-view/', views.staffAnnouncementView,
         name='staffAnnouncementView'),
    path('post-announcement/', views.postAnnouncement, name='postAnnouncement'),

    path('complain-student-view/', views.complainStudentView,
         name='complainStudentView'),
    path('complain-staff-view/', views.complainStaffView, name='complainStaffView'),
    path('post-complain/', views.postComplain, name='postComplain'),


    # ---------------------------------------------------#
    path('approval-staff-view/', views.staff_pending_request_view,
         name="approve_request_pending"),
    path('approve-student/<int:id>', views.approve_student,
         name="approve_request_confirmation"),

    # -----------------Module 4-----------------------#
    path('staff-faculty-list/', views.see_faculty_list, name='staff_see_faculty'),
    path('staff-faculty-update/<int:id>', views.update_faculty, name='staff_update_faculty'),
    path('staff-add-faculty/', views.add_faculty, name='staff_add_faculty'),
    path('student_advising/', views.student_advising, name="student_advising"),
    path('make_request/', views.make_request, name='make_request'),
    path('request_list/', views.request_list, name='request_list'),
    path('view-enrolled-courses/', views.student_view_course, name="student_enrolled_courses"),
    path('download-payslip/', views.generate_payslip, name='download_payslip'),
    path('make-routine/<int:id>', views.make_routine, name='make_routine'),
    path('modify-course/<int:id>', views.faculty_modify_course, name='modify_course'),
    path('make-exam-routine/<int:id>', views.make_exam_routine, name='make_exam_routine'),
    path('view-routine/', views.student_view_routine, name='student_view_routine'),
    path('recover-password/', views.password_recover , name='recover_password'),

    path('faculty-add-course/', views.add_course, name="faculty_add_course"),
    path('recover-password-confirm/', views.password_recover_confirm , name='recover_password_confirm'),
    path('student-course-announcements/', views.student_view_course_announcement , name='student_course_announcements'),

]

