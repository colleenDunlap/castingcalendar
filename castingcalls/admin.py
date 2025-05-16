from django.contrib import admin
from .models import Casting, Calendar, CalendarItem
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(Casting)
admin.site.register(CalendarItem)
admin.site.register(Calendar)
