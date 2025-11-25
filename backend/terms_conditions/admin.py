#########################################
"""
ADMIN UI DESIGN SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from terms_conditions.models import TermsConditionTopBar, TermsConditionContent

class TermsConditionTopBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'edit_link', 'delete_link')

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/terms_conditions/termsconditiontopbar/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/terms_conditions/termsconditiontopbar/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

class TermsConditionContentAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'edit_link', 'delete_link')

    def content_preview(self, obj):
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_preview.short_description = 'Content'

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/terms_conditions/termsconditioncontent/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/terms_conditions/termsconditioncontent/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# REGISTER MODELS HERE.
admin.site.register(TermsConditionTopBar, TermsConditionTopBarAdmin)
admin.site.register(TermsConditionContent, TermsConditionContentAdmin)
