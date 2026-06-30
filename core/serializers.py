from rest_framework.serializers import ModelSerializer
from core.models import Teacher, Candidate, Subject, Department, QuestionSet, Exam
from django.contrib.auth import get_user_model

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'role']


class TeacherSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Teacher
        fields=['user', 'age', 'description']

class SubjectSerializer(ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class QuestionSetSerializer(ModelSerializer):
    class Meta:
        model=QuestionSet
        fields='__all__'

class ExamSerializer(ModelSerializer):
    subject=SubjectSerializer(read_only=True)
    department=DepartmentSerializer(read_only=True)
    ques_ans_set=QuestionSetSerializer(many=True, read_only=True)
    class Meta:
        model=Exam
        fields='__all__'

class CandidateSerializer(ModelSerializer):
    class Meta:
        model=Candidate
        fields=['user', 'rollno', 'date_of_birth', 'exams']