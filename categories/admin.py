from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'paper_count', 'created_at', 'actions_buttons')
    list_filter = ('created_at',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(paper_count=Count('papers'))
    
    def paper_count(self, obj):
        return obj.paper_count
    paper_count.short_description = 'Papers'
    paper_count.admin_order_field = 'paper_count'
    
    def actions_buttons(self, obj):
        # Check if category has papers
        if obj.papers.exists():
            return format_html(
                '<span title="Cannot delete category with papers" style="color: #666; padding: 5px 10px; '
                'background: #f2f2f2; border-radius: 5px;">Protected</span>'
            )
        return format_html(
            '<a class="button" href="{}/delete/" style="background: #ba2121; padding: 5px 10px; '
            'color: #fff; border-radius: 5px; text-decoration: none;">Remove</a>',
            obj.id
        )
    actions_buttons.short_description = 'Actions'
    actions_buttons.allow_tags = True
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            actions['delete_selected'] = (
                actions['delete_selected'][0],
                'delete_selected',
                'Remove selected categories'
            )
        return actions
