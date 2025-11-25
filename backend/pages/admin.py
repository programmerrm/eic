#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from pages.models import (
    Pages,
    SEOKeyword,
    OpenGraphMetaTags,
    TwitterCardMetaTags,
    AdditionalSEOFields,
)

class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'edit_link', 'delete_link')
    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/pages/pages/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/pages/pages/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# REGISTER MODELS HERE.
admin.site.register(Pages, PagesAdmin)

admin.site.register(SEOKeyword)
admin.site.register(OpenGraphMetaTags)
admin.site.register(TwitterCardMetaTags)
admin.site.register(AdditionalSEOFields)
