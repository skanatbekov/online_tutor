from rest_framework import serializers

from .models import User, Category, Mentor, Student, SendRequest


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendRequest
        fields = '__all__'

