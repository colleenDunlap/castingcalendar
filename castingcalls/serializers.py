from rest_framework import serializers
from .models import Calendar, CalendarItem, Casting

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'user', 'is_public')

class CastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting
        fields = ('id', 'title', 'producer', 'producer_name', 'production_company', 
                 'description', 'submission_due_date', 'show_date', 'submission_link', 
                 'style', 'is_published')

class CalendarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarItem
        fields = ('id', 'name', 'user', 'description', 'casting', 'calendar', 'is_complete')