from django.contrib import admin
from .models import EventInsert

class AdminEvent(admin.ModelAdmin):
    list_display = ['from_currency', 'target_currency', 'from_price', 'target_price', 'time_inserted']

admin.site.register(EventInsert, AdminEvent)