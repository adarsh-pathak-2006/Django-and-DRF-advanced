from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User=get_user_model()

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role=='TEACHER')
    
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role=='STUDENT')
    
class IsStudentAndTeacher(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.TEACHER, User.STUDENT])
