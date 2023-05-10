from django.contrib.auth.models import User
from rest_framework import viewsets, status, mixins, generics, permissions, views
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import filters


from .permissions import IsPermitted, IsSuper
from .models import Course, Mentor, Student, SendRequest
from .serializers import UserRegisterSerializer, CourseSerializer, MentorSerializer, StudentSerializer, \
    StudentSendRequestSerializer


class CourseListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CourseCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsSuper, ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseRetrieveAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CourseUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsSuper, ]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'experience']
    ordering_fields = ['rate', ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MentorCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermitted, ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MentorRetrieveAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MentorUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermitted, ]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermitted, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['birth_date', ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermitted, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentSendRequestAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = SendRequest.objects.all()
    serializer_class = StudentSendRequestSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})