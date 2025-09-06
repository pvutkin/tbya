"""
Models for jobs application.
"""

from django.db import models
from django.urls import reverse
from tags.models import Tag

class Job(models.Model):
    """
    Model representing a job vacancy.
    """
    title = models.CharField(max_length=200, verbose_name='Название вакансии')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    salary = models.CharField(max_length=100, blank=True, verbose_name='Зарплата')
    description = models.TextField(verbose_name='Описание вакансии')
    external_url = models.URLField(max_length=500, verbose_name='Внешняя ссылка для отклика')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('jobs:job_detail', kwargs={'slug': self.slug})