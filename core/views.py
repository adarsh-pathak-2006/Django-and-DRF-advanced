from django.shortcuts import render, get_object_or_404
from core.serializers import *
from core.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from core.permissions import IsStudent, IsTeacher, IsStudentAndTeacher
from rest_framework.permissions import IsAuthenticated


User=get_user_model()

class CandidateAPI(ListCreateAPIView):
    serializer_class=CandidateSerializer

    def get_queryset(self):
        if self.request.user.role==User.TEACHER:
            return Candidate.objects.all()
        return Candidate.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        if self.request.method=='GET':
            return [IsStudentAndTeacher()]
        return [IsTeacher()]

class CandidateAPIDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=CandidateSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsTeacher()]
        return [IsStudentAndTeacher()]
    
    def get_queryset(self):
        if self.request.user.role==User.TEACHER:
            return Candidate.objects.all()
        return Candidate.objects.filter(user=self.request.user)