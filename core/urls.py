from django.urls import path
from core.views import *

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('candidate/', CandidateAPI.as_view(), name='candidate'),
    path('candidate/<int:pk>/', CandidateAPIDetail.as_view(), name='candidate_individual'),
    path('teacher/', TeacherAPI.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherAPIDetail.as_view(), name='teacher_individual'),
    path('exam/', ExamAPI.as_view(), name='exam'),
    path('exam/<int:pk>/', ExamAPIDetail.as_view(), name='exam_individual'),
]