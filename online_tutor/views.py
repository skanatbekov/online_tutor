from rest_framework import viewsets, status, mixins, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .permissions import IsPermitted, IsPermittedObj, IsSuper, IsSuperObj
from .models import Course, Mentor, Student
from .serializers import UserRegisterSerializer, CourseSerializer, MentorSerializer, StudentSerializer


class CourseListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CourseCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuper, ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsSuperObj, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MentorCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermitted, ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MentorRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsPermittedObj, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsPermitted, ]

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
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsPermittedObj, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=['POST', ])
def user_register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

