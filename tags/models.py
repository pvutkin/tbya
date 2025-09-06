"""
Models for tags application.
"""

from django.db import models

class Tag(models.Model):
    """
    Model representing a tag.
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']
    
    def __str__(self):
        return self.name