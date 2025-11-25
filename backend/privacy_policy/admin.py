#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from privacy_policy.models import PrivacyPolicyTopBar, PrivacyPolicyContent

class PrivacyPolicyTopBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_link', 'delete_link')

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/privacy_policy/privacypolicytopbar/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/privacy_policy/privacypolicytopbar/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

class PrivacyPolicyContentAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'edit_link', 'delete_link')

    def content_preview(self, obj):
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_preview.short_description = 'Content'

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/privacy_policy/privacypolicycontent/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/privacy_policy/privacypolicycontent/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# REGISTER MODELS HERE.
admin.site.register(PrivacyPolicyTopBar, PrivacyPolicyTopBarAdmin)
admin.site.register(PrivacyPolicyContent, PrivacyPolicyContentAdmin)
