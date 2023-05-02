from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('course/', views.CourseListAPIView.as_view()),
    path('course/create', views.CourseCreateAPIView.as_view()),
    path('course/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),

    path('mentor/', views.MentorListAPIView.as_view()),
    path('mentor/create/', views.MentorCreateAPIView.as_view()),
    path('mentor/<int:pk>/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),

    path('student/', views.StudentListAPIView.as_view()),
    path('student/create/', views.StudentCreateAPIView.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('register/', views.user_register),
    path('auth_token/', auth_views.obtain_auth_token)

]
