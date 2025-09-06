"""
Views for tbya_portal project.
"""

from django.shortcuts import render
from jobs.models import Job
from courses.models import Course
from blog.models import Post

def home(request):
    """
    View for the home page.
    """
    # Get latest jobs (6-8)
    latest_jobs = Job.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    # Get popular courses (6-8)
    popular_courses = Course.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    # Get latest blog posts (3-4)
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')[:4]
    
    context = {
        'latest_jobs': latest_jobs,
        'popular_courses': popular_courses,
        'latest_posts': latest_posts,
    }
    
    return render(request, 'home.html', context)