from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('course/', views.CourseListCreateAPIView.as_view()),
    path('course/create/', views.CourseListCreateAPIView.as_view()),
    path('course/<int:pk>/detail/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),
    path('course/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),

    path('mentor/', views.MentorListCreateAPIView.as_view()),
    path('mentor/create/', views.MentorListCreateAPIView.as_view()),
    path('mentor/<int:pk>/detail/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),
    path('mentor/<int:pk>/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),

    path('student/', views.StudentListAPIView.as_view()),
    path('student/create/', views.StudentCreateAPIView.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('student/request/', views.StudentSendRequestAPIView.as_view()),

    path('register/', views.UserRegisterAPIView.as_view()),
    path('auth_token/', auth_views.obtain_auth_token)

]
