from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentLogin, name='studentLogin'),
    path('index/', views.index, name='index'),

]