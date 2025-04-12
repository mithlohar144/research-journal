from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'actions_buttons')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional Info', {'fields': ('role', 'bio', 'institution')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    def actions_buttons(self, obj):
        if obj.is_superuser:  # Don't show delete button for superusers
            return format_html('<span style="color: #666;">Protected</span>')
        return format_html(
            '<a class="button" href="{}/delete/" style="background: #ba2121; padding: 5px 10px; '
            'color: #fff; border-radius: 5px; text-decoration: none;">Remove</a>',
            obj.id
        )
    actions_buttons.short_description = 'Actions'
    actions_buttons.allow_tags = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:  # Rename bulk delete action
            actions['delete_selected'] = (
                actions['delete_selected'][0],
                'delete_selected',
                'Remove selected users'
            )
        return actions

# Register the custom admin class
admin.site.register(User, CustomUserAdmin)
