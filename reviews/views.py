from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from papers.models import ResearchPaper
from .models import PaperReview
from .forms import ReviewForm

# Create your views here.

@login_required
def review_create(request, paper_slug):
    paper = get_object_or_404(ResearchPaper, slug=paper_slug)
    
    # Check if user has already reviewed this paper
    if PaperReview.objects.filter(paper=paper, reviewer=request.user).exists():
        messages.error(request, 'You have already reviewed this paper.')
        return redirect('papers:detail', slug=paper_slug)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.paper = paper
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Your review has been submitted successfully.')
            return redirect('papers:detail', slug=paper_slug)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review_form.html', {
        'form': form,
        'paper': paper
    })

def review_list(request, paper_slug):
    paper = get_object_or_404(ResearchPaper, slug=paper_slug)
    reviews = paper.reviews.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {
        'paper': paper,
        'reviews': reviews
    })
