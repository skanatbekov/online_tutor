from rest_framework import serializers
from django.contrib.auth import password_validation as pv
from django.contrib.auth.models import User as djuser


from .models import User, Course, Mentor, Student, SendRequest


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, write_only=True)
    password2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_password(self, value):
        try:
            pv.validate_password(value)
        except pv.ValidationError as e:
            raise serializers.ValidationError(e)
        else:
            return value

    def create(self, validated_data):
        user = djuser(username=validated_data['username'])
        user.set_password(validated_data['password'])
        if user.username.startswith('tutor.'):
            user.is_staff = True
        else:
            user.is_staff = False

        if user.username.startswith('admin.'):
            user.is_superuser = True
        else:
            user.is_superuser = False
        user.save()
        return user


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
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

