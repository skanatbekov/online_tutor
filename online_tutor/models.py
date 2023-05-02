from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    experience = models.CharField(max_length=50)
    rate = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')
    avatar = models.ImageField(default='profile/default-avatar.png', upload_to='profile')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SendRequest(models.Model):
    fullname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.fullname




