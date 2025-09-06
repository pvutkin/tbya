"""
Views for blog application.
"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    """
    View for the blog post list page.
    """
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """
    View for the blog post detail page.
    """
    post = get_object_or_404(Post, slug=slug, is_published=True)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog/post_detail.html', context)