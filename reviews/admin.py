from django.contrib import admin
from .models import PaperReview

# Register your models here.

@admin.register(PaperReview)
class PaperReviewAdmin(admin.ModelAdmin):
    list_display = ('paper', 'reviewer', 'decision', 'created_at')
    list_filter = ('decision', 'created_at')
    search_fields = ('paper__title', 'reviewer__username', 'comments')
