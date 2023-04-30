from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('course/', views.CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/<int:pk>/', views.CourseViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

    path('mentor/', views.MentorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('mentor/<int:pk>/', views.MentorViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

    path('student/', views.StudentListAPIView.as_view()),
    path('student/create/', views.StudentCreateAPIView.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('register/', views.user_register),
    path('auth_token/', auth_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls')),

]
