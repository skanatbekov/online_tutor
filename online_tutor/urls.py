from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

router = routers.DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('mentor', views.MentorViewSet)
router.register('student', views.StudentListCreateAPIView)
router.register('student/<int: pk>', views.StudentRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.user_register),
    path('auth_token/', auth_views.obtain_auth_token),
]
