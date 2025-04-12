from django.shortcuts import render
from papers.models import ResearchPaper
from categories.models import Category
from taggit.models import Tag

def home(request):
    latest_papers = ResearchPaper.objects.filter(status='approved').order_by('-created_at')[:5]
    categories = Category.objects.all()
    papers = ResearchPaper.objects.filter(status='approved')
    tags = Tag.objects.all()[:20]  # Get top 20 tags
    
    return render(request, 'home.html', {
        'latest_papers': latest_papers,
        'categories': categories,
        'papers': papers,
        'tags': tags,
    })
