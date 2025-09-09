from rest_framework import serializers
from .models import Board, Column, Card
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CardSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assignee', write_only=True, required=False
    )

    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'assignee', 'assignee_id',
                  'labels', 'due_date', 'order', 'column']

class ColumnSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = ['id', 'title', 'order', 'board', 'cards']

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'owner', 'created_at', 'columns']
