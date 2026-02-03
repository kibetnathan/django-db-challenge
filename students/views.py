from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, exceptions
from .models import Student, UserProfile
from .serializers import StudentSerializer
from django.db import IntegrityError

# Create your views here.

class StudentView(APIView):
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        result = Student.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"status": "success", "data": "Student deleted"}, status=status.HTTP_200_OK)
    
class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise exceptions.NotFound(f"Student with ID {pk} not found.")

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError:
                return Response({"detail": "Invalid data."}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def create_profile(request):
    user_profile = UserProfile.objects.create(
        username= 'Joseph',
        email = 'jay@example.com',
        ssn = '123-24-6789',
        bio = 'This is a bio about Toseph'
    )
    
    print(user_profile.ssn)
    print(user_profile.bio)
    return(render(user_profile))