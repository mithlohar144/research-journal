from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    AUTHOR = 'author'
    REVIEWER = 'reviewer'
    ADMIN = 'admin'
    
    ROLE_CHOICES = [
        (AUTHOR, 'Author'),
        (REVIEWER, 'Reviewer'),
        (ADMIN, 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=AUTHOR)
    bio = models.TextField(max_length=500, blank=True)
    institution = models.CharField(max_length=200, blank=True)
    
    def is_reviewer_or_admin(self):
        return self.role in [self.REVIEWER, self.ADMIN]
