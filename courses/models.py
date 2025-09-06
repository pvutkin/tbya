"""
Models for courses application.
"""

from django.db import models
from django.urls import reverse
from tags.models import Tag

class Course(models.Model):
    """
    Model representing a course.
    """
    title = models.CharField(max_length=200, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    description = models.TextField(verbose_name='Описание курса')
    external_url = models.URLField(max_length=500, verbose_name='Внешняя ссылка на курс')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={'slug': self.slug})