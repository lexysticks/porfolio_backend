from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

# API view to list all projects
class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
