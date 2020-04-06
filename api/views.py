from django.shortcuts import render
from rest_framework import generics, filters
from .models import ToDo
from .serializers import ToDoSerializer
# Create your views here.

class ToDoListCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['task']
    ordering_fields = ['created_datetime', 'is_complete']