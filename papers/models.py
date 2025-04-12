from django.db import models
from django.conf import settings
from django.utils.text import slugify
from taggit.managers import TaggableManager
from categories.models import Category
from django.utils import timezone

# Create your models here.

def paper_file_path(instance, filename):
    return f'papers/{instance.author.username}/{filename}'

class ResearchPaper(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    abstract = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='papers')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='papers')
    pdf_file = models.FileField(upload_to=paper_file_path)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            # Keep checking until we find a unique slug
            while ResearchPaper.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def is_editable(self):
        return self.status == 'pending'
