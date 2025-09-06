"""
Views for analytics application.
"""

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import ClickEvent
from jobs.models import Job
from courses.models import Course

@staff_member_required
def analytics_dashboard(request):
    """
    View for the analytics dashboard.
    """
    # Total clicks
    total_clicks = ClickEvent.objects.count()
    
    # Clicks by type
    clicks_by_type = ClickEvent.objects.values('click_type').annotate(count=Count('click_type'))
    
    # Top jobs by clicks
    top_jobs = Job.objects.annotate(click_count=Count('clickevent')).order_by('-click_count')[:10]
    
    # Top courses by clicks
    top_courses = Course.objects.annotate(click_count=Count('clickevent')).order_by('-click_count')[:10]
    
    context = {
        'total_clicks': total_clicks,
        'clicks_by_type': clicks_by_type,
        'top_jobs': top_jobs,
        'top_courses': top_courses,
    }
    
    return render(request, 'analytics/dashboard.html', context)