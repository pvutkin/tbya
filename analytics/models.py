"""
Models for analytics application.
"""

from django.db import models
from jobs.models import Job
from courses.models import Course

class ClickEvent(models.Model):
    """
    Model representing a click event (job application or course enrollment).
    """
    CLICK_TYPE_CHOICES = [
        ('job_application', 'Отклик на вакансию'),
        ('course_enrollment', 'Запись на курс'),
    ]
    
    click_type = models.CharField(max_length=20, choices=CLICK_TYPE_CHOICES, verbose_name='Тип клика')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Вакансия')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Курс')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время клика')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    user_agent = models.TextField(blank=True, verbose_name='User Agent')
    
    class Meta:
        verbose_name = 'Событие клика'
        verbose_name_plural = 'События кликов'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.click_type} - {self.timestamp}"