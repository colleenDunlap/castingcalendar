from django.contrib import admin
from .models import Casting, Calendar, CalendarItem

admin.site.register(Casting)
admin.site.register(CalendarItem)
admin.site.register(Calendar)
