"""
Admin configuration for jobs application.
"""

from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'is_active', 'created_at')
    list_filter = ('is_active', 'tags', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)