from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ResearchPaper
from .forms import PaperForm
from categories.models import Category
from taggit.models import Tag

# Create your views here.

def paper_list(request, slug=None, tag_slug=None):
    papers = ResearchPaper.objects.filter(status='approved')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    category = None
    tag = None
    
    if slug:
        category = get_object_or_404(Category, slug=slug)
        papers = papers.filter(category=category)
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        papers = papers.filter(tags__in=[tag])
    
    search_query = request.GET.get('q')
    if search_query:
        papers = papers.filter(title__icontains=search_query)
    
    category_slug = request.GET.get('category')
    if category_slug:
        papers = papers.filter(category__slug=category_slug)
    
    return render(request, 'papers/paper_list.html', {
        'papers': papers,
        'categories': categories,
        'category': category,
        'tag': tag,
        'tags': tags
    })

def paper_detail(request, slug):
    paper = get_object_or_404(ResearchPaper, slug=slug)
    related_papers = ResearchPaper.objects.filter(category=paper.category).exclude(id=paper.id)[:3]
    return render(request, 'papers/paper_detail.html', {
        'paper': paper,
        'related_papers': related_papers
    })

@login_required
def paper_submit(request):
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.author = request.user
            paper.save()
            form.save_m2m()  # Save tags
            messages.success(request, 'Your paper has been submitted successfully!')
            return redirect('papers:detail', slug=paper.slug)
    else:
        form = PaperForm()
    
    return render(request, 'papers/paper_form.html', {'form': form})
