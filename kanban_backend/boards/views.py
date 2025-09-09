from rest_framework import viewsets, permissions
from .models import Board, Column, Card
from .serializers import BoardSerializer, ColumnSerializer, CardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]
