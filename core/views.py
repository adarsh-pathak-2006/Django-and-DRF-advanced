from django.shortcuts import render, redirect
from core.serializers import *
from core.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from core.permissions import IsTeacher, IsStudentAndTeacher
from django.views import View
from core.forms import *


User=get_user_model()


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']
            role=form_data.cleaned_data['role']

            if pass1==pass2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'form': form_data,'user_err':'user already exists' })
                else:
                    User.objects.create_user(username=name, password=pass1, role=role)
                    return redirect('register')
            else:
                return render(request, 'register.html', { 'form': form_data, 'pass_err':'enter the same password in both fields' })
        else:
            return render(request, 'register.html', { 'form': form_data, 'invalid':'invalid input' })    

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
    
class TeacherAPI(ListCreateAPIView):
    permission_classes=[IsTeacher]
    serializer_class=TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)
    
class TeacherAPIDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsTeacher]
    serializer_class=TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)
    
class ExamAPI(ListCreateAPIView):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsStudentAndTeacher()]
        return [IsTeacher()]
    
class ExamAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer

    def get_permissions(self):
        if self.request.method=='GET':
            return [IsStudentAndTeacher()]
        return [IsTeacher()]
