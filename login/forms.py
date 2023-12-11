from django import forms
from .models import *

class FacultyCreationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = ['joined_date']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'faculty_initial':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
        }


class RoutineCreationForm(forms.ModelForm):
    class Meta:
        model = ClassRoutine
        fields = '__all__'
        exclude = ['instructor', 'course']
        widgets = {
            'day':forms.Select(attrs={'class':'form-control'}),
            'start_time':forms.TimeInput(attrs={'class':'form-control'}),
            'end_time':forms.TimeInput(attrs={'class':'form-control'}),
        }

class ExamRoutineCreationForm(forms.ModelForm):
    class Meta:
        model = ExamRoutine
        fields = '__all__'
        exclude = ['instructor', 'course']
        widgets = {
            'day':forms.Select(attrs={'class':'form-control'}),
            'start_time':forms.TimeInput(attrs={'class':'form-control', 'placeholder':'HH:MM'}),
            'end_time':forms.TimeInput(attrs={'class':'form-control', 'placeholder':'HH:MM'}),
            'date':forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
        }

class CourseUpdationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = ["course_faculty", "start_time", "end_time", "course_fee","course_credit", "course_department"]
        widgets = {
            "course_id":forms.TextInput(attrs={'class':'form-control'}),
            "course_name":forms.TextInput(attrs={'class':'form-control'}),
            "course_description":forms.Textarea(attrs={'class':'form-control'}),
        }

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            'student_id':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'enrolled_semester':forms.TextInput(attrs={'class':'form-control'}),
            'is_approved':forms.CheckboxInput()
        }

class CourseAnnouncementForm(forms.ModelForm):
    class Meta:
        model = CourseAnnouncement
        fields = "__all__"
        exclude = ['posted_by']
        widgets = {
            'statement':forms.Textarea(attrs={'class':'form-control'}),
            'course':forms.Select(attrs={'class':'form-control'}),
        }
    
    def __init__(self, faculty, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(course_faculty=faculty)


class FacultyUpdationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = ["user", "joined_date"]
        widgets = {
            'faculty_initial': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }