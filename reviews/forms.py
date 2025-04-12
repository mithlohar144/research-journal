from django import forms
from .models import PaperReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = PaperReview
        fields = ['rating', 'comments']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
