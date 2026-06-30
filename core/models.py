from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views import View


class User(AbstractUser):
    TEACHER='TEACHER'
    STUDENT='STUDENT'

    ROLE_CHOICES=[(TEACHER, 'Teacher'), (STUDENT, 'Student')]

    role=models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)

class Subject(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name=models.CharField(max_length=80)
    code=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class QuestionSet(models.Model):
    question=models.TextField()
    option1=models.TextField()
    option2=models.TextField()
    option3=models.TextField()
    option4=models.TextField()
    correct_answer=models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    marks=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question[:80]

class Exam(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    ques_ans_set=models.ManyToManyField(QuestionSet)

    def __str__(self):
        return self.subject.name


class Candidate(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    rollno=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    exams=models.ManyToManyField(Exam, blank=True)

    def __str__(self):
        return self.rollno
    
class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    description=models.TextField()
    
    def __str__(self):
        return self.user.username