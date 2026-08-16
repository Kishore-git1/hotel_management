from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Food
from .serializers import FoodSerializer

print("hello")
class FoodViewSet(viewsets.ModelViewSet):

    queryset = Food.objects.all()

    serializer_class = FoodSerializer

    permission_classes = [IsAuthenticated]
