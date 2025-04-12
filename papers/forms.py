from django import forms
from .models import ResearchPaper

class PaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'abstract', 'category', 'pdf_file', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your paper'
            }),
            'abstract': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Provide a brief summary of your research'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'pdf_file': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tags separated by commas'
            })
        }
