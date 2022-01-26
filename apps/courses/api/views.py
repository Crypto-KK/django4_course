from rest_framework import generics
from .serializers import SubjectSerializer, CourseSerializer
from ..models import Subject, Course


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer