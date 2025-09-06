"""
Views for jobs application.
"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Job
from tags.models import Tag

def job_list(request):
    """
    View for the job list page.
    """
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    
    # Get filter parameters
    tag_ids = request.GET.getlist('tags')
    has_salary = request.GET.get('has_salary')
    
    # Apply filters
    if tag_ids:
        jobs = jobs.filter(tags__id__in=tag_ids).distinct()
    
    if has_salary:
        jobs = jobs.exclude(salary='')
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all tags for filter
    all_tags = Tag.objects.all()
    
    context = {
        'page_obj': page_obj,
        'all_tags': all_tags,
        'selected_tags': [int(tag_id) for tag_id in tag_ids] if tag_ids else [],
        'has_salary': has_salary,
    }
    
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, slug):
    """
    View for the job detail page.
    """
    job = get_object_or_404(Job, slug=slug, is_active=True)
    
    # Get recommended courses (same tags)
    job_tags = job.tags.all()
    recommended_courses = job_tags.first().course_set.filter(is_active=True)[:3] if job_tags.exists() else []
    
    context = {
        'job': job,
        'recommended_courses': recommended_courses,
    }
    
    return render(request, 'jobs/job_detail.html', context)