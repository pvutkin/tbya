"""
Admin configuration for analytics application.
"""

from django.contrib import admin
from .models import ClickEvent

@admin.register(ClickEvent)
class ClickEventAdmin(admin.ModelAdmin):
    list_display = ('click_type', 'job', 'course', 'timestamp', 'ip_address')
    list_filter = ('click_type', 'timestamp')
    search_fields = ('ip_address', 'user_agent')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)