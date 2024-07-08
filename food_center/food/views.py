from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import FoodType,Composition,Food,Comment
from .serializers import FoodTypeSerializer,CompositionSerializer,FoodSerializer,CommentSerializer
from .permissions import FoodPermission,CommentPermission


class FoodTypeApiView(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [FoodPermission]


class CompositionApiView(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = [FoodPermission]


class FoodApiView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [FoodPermission]


class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]