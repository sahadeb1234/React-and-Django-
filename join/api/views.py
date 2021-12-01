from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.serializers import Serializer

from api.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
 
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
     