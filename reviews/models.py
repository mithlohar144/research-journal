from django.db import models
from django.conf import settings
from papers.models import ResearchPaper

# Create your models here.

class PaperReview(models.Model):
    DECISION_CHOICES = [
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('revise', 'Request Revision'),
    ]
    
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    paper = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    comments = models.TextField()
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['paper', 'reviewer']
    
    def __str__(self):
        return f'Review by {self.reviewer.username} for {self.paper.title}'
    
    def save(self, *args, **kwargs):
        if self.decision in ['approve', 'reject']:
            self.paper.status = 'approved' if self.decision == 'approve' else 'rejected'
            self.paper.save()
        super().save(*args, **kwargs)
