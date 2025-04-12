from django.contrib import admin
from django.utils.html import format_html
from .models import ResearchPaper

# Register your models here.

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'actions_buttons')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'abstract', 'author__username', 'author__email')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = ['approve_papers', 'reject_papers']
    
    def actions_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}/delete/" style="background: #ba2121; padding: 5px 10px; color: #fff; border-radius: 5px; text-decoration: none;">Delete</a>',
            obj.id
        )
    actions_buttons.short_description = 'Actions'
    actions_buttons.allow_tags = True
    
    def approve_papers(self, request, queryset):
        queryset.update(status='approved')
    approve_papers.short_description = "Mark selected papers as approved"
    
    def reject_papers(self, request, queryset):
        queryset.update(status='rejected')
    reject_papers.short_description = "Mark selected papers as rejected"
