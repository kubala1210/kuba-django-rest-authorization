from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Name:
        model = Note
        fields = ['id', 'title', 'content', 'owner', 'created_at']
