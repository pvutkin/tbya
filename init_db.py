#!/usr/bin/env python
"""
Script to initialize the database for the TBYA portal.
"""

import os
import django
from django.core.management import execute_from_command_line

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbya_portal.settings')
django.setup()

if __name__ == '__main__':
    # Run migrations
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser (optional)
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        print("Superuser 'admin' created with password 'adminpassword'")
    else:
        print("Superuser 'admin' already exists")
    
    print("Database initialized successfully!")