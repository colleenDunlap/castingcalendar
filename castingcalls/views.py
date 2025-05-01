from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CalendarSerializer, CastingSerializer, CalendarItemSerializer
from .models import Calendar, CalendarItem, Casting

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the castings index.")

class CastingView(viewsets.ModelViewSet):
    serializer_class = CastingSerializer
    queryset = Casting.objects.all()

class CalendarItemView(viewsets.ModelViewSet):
    serializer_class = CalendarItemSerializer
    queryset = CalendarItem.objects.all()

class CalendarView(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()