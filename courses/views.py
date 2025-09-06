"""
Views for courses application.
"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Course
from tags.models import Tag

def course_list(request):
    """
    View for the course list page.
    """
    courses = Course.objects.filter(is_active=True).order_by('-created_at')
    
    # Get filter parameters
    tag_ids = request.GET.getlist('tags')
    
    # Apply filters
    if tag_ids:
        courses = courses.filter(tags__id__in=tag_ids).distinct()
    
    # Pagination
    paginator = Paginator(courses, 10)  # Show 10 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all tags for filter
    all_tags = Tag.objects.all()
    
    context = {
        'page_obj': page_obj,
        'all_tags': all_tags,
        'selected_tags': [int(tag_id) for tag_id in tag_ids] if tag_ids else [],
    }
    
    return render(request, 'courses/course_list.html', context)

def course_detail(request, slug):
    """
    View for the course detail page.
    """
    course = get_object_or_404(Course, slug=slug, is_active=True)
    
    context = {
        'course': course,
    }
    
    return render(request, 'courses/course_detail.html', context)