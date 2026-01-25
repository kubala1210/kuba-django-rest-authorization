from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from .permissions import ACLPermissions


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, ACLPermissions]


class NoteListCreate(generics.ListCreateAPIView):

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# Create your views here.
