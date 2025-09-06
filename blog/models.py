"""
Models for blog application.
"""

from django.db import models
from django.urls import reverse

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')
    excerpt = models.TextField(blank=True, verbose_name='Анонс')
    content = models.TextField(verbose_name='Полный текст')
    cover_image = models.ImageField(upload_to='blog/covers/', blank=True, verbose_name='Обложка')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})