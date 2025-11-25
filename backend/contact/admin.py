#########################################
"""
ADMIN UI DESIGN SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from contact.models import ContactTopBar, ContactForm, ConatctInfomation, GoogleMap, Schema, SeoTag

# ========== SEO TAG TOP BAR ADMIN ==========
class SeoTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

# ========== SCHEMA TOP BAR ADMIN ==========
class SchemaAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'url', 'contact_type', 'email', 'phone_number', 'created_at', 'updated_at')

# ========== CONTACT TOP BAR ADMIN ==========
class ContactTopBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'image_preview', 'edit_link', 'delete_link')
    search_fields = ('title',)
    list_filter = ('title',)

    def description_short(self, obj):
        return obj.description[:50] + ('...' if len(obj.description) > 50 else '')
    description_short.short_description = "Short Description"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" style="object-fit:cover;"/>')
        return "No Image"
    image_preview.short_description = "Image Preview"

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/contacttopbar/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/contacttopbar/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# ========== CONTACT FORM ADMIN ==========
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'company_name', 'message_short')
    search_fields = ('full_name', 'email', 'company_name')
    list_filter = ('company_name',)

    def message_short(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    message_short.short_description = "Short Message"

# ========== CONTACT INFORMATION ADMIN ==========
class ConatctInfomationAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'address', 'phone_number1', 'phone_number2', 'edit_link', 'delete_link')
    search_fields = ('title', 'email', 'address')
    list_filter = ('title', 'email')

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/conatctinfomation/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/conatctinfomation/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# ========== GOOGLE MAP ADMIN ==========
class GoogleMapAdmin(admin.ModelAdmin):
    list_display = ('url', 'edit_link', 'delete_link')
    search_fields = ('url',)
    list_filter = ('url',)

    def edit_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/googlemap/{obj.id}/change/">Edit</a>')
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        return mark_safe(f'<a href="/admin/contact/googlemap/{obj.id}/delete/">Delete</a>')
    delete_link.short_description = 'Delete'

# REGISTER MODELS HERE
admin.site.register(ContactTopBar, ContactTopBarAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ConatctInfomation, ConatctInfomationAdmin)
admin.site.register(GoogleMap, GoogleMapAdmin)
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
