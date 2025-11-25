# #########################################
# """
# ADMIN UI DESIGN SETUP
# """
# #########################################
from django.contrib import admin, messages
from django.utils.html import format_html
from django.urls import path, reverse
from django.shortcuts import redirect
from services.models import ServicePageTopBar, Service, Categories, Faq, FaqItem, ServiceItemMain, ServiceItem, ServicesIncludeTopTitle, ServicesIncludeTopItem, ServicesIncludeBottomTitle, ServicesIncludeBottomItem
from django import forms
from django.db import models


# @admin.register(Services)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = (
#         'styled_name',
#         'styled_slug',
#         'styled_description',
#         'image_preview',
#         'bg_image_preview',
#         'edit_link',
#         'delete_link',
#     )

#     readonly_fields = ('slug', 'image_preview', 'bg_image_preview')

#     fields = (
#         'name',
#         'slug',
#         'description',
#         'image',
#         'bg',
#         'image_preview',
#         'bg_image_preview',
#     )

#     formfield_overrides = {
#         models.CharField: {
#             'widget': forms.TextInput(
#                 attrs={
#                     'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
#                 }
#             )
#         },
#         models.TextField: {
#             'widget': forms.Textarea(
#                 attrs={
#                     'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
#                 }
#             )
#         },
#     }

#     # ==============================
#     # 🔹 Custom URL for image delete
#     # ==============================
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path(
#                 '<int:service_id>/delete-image/',
#                 self.admin_site.admin_view(self.delete_image_view),
#                 name='services_service_delete_image',
#             ),
#             path(
#                 '<int:service_id>/delete-bg/',
#                 self.admin_site.admin_view(self.delete_bg_view),
#                 name='services_service_delete_bg',
#             ),
#         ]
#         return custom_urls + urls

#     # ✅ Delete main image
#     def delete_image_view(self, request, service_id):
#         service = Services.objects.get(pk=service_id)
#         if service.image:
#             service.image.delete(save=False)
#             service.image = None
#             service.save()
#             self.message_user(request, "✅ Image deleted successfully.", messages.SUCCESS)
#         else:
#             self.message_user(request, "⚠ No image to delete.", messages.WARNING)
#         return redirect(reverse('admin:services_services_change', args=[service_id]))

#     # ✅ Delete background image
#     def delete_bg_view(self, request, service_id):
#         service = Services.objects.get(pk=service_id)
#         if hasattr(service, 'bg') and service.bg:
#             service.bg.delete(save=False)
#             service.bg = None
#             service.save()
#             self.message_user(request, "✅ Background image deleted successfully.", messages.SUCCESS)
#         else:
#             self.message_user(request, "⚠ No background image to delete.", messages.WARNING)
#         return redirect(reverse('admin:services_services_change', args=[service_id]))

#     # ==============================
#     # 🔹 Styled Fields
#     # ==============================
#     def styled_name(self, obj):
#         return format_html(
#             '<div style="border:1px solid #ccc; border-radius:6px; padding:6px; background:#f9f9f9;">{}</div>',
#             obj.name,
#         )
#     styled_name.short_description = "Service Name"

#     def styled_slug(self, obj):
#         return format_html(
#             '<div style="border:1px solid #ccc; border-radius:6px; padding:6px; background:#fcfcfc;">{}</div>',
#             obj.slug,
#         )
#     styled_slug.short_description = "Slug"

#     def styled_description(self, obj):
#         text = obj.description or "No Description"
#         return format_html(
#             '<div style="border:1px solid #ccc; border-radius:6px; padding:6px; background:#fdfdfd; '
#             'max-width:400px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{}</div>',
#             text,
#         )
#     styled_description.short_description = "Description"

#     # ==============================
#     # 🔹 Main Image Preview
#     # ==============================
#     def image_preview(self, obj):
#         if obj.image:
#             delete_url = reverse('admin:services_service_delete_image', args=[obj.id])
#             return format_html(
#                 '''
#                 <div style="border:1px solid #ccc; border-radius:8px; padding:4px; display:inline-block; text-align:center;">
#                     <img src="{}" style="width:50px; height:auto; border-radius:6px; box-shadow:0 0 5px rgba(0,0,0,0.1);" />
#                 </div>
#                 ''',
#                 obj.image.url,
#                 delete_url,
#             )
#         return format_html('<span style="color:#999;">No image uploaded</span>')
#     image_preview.short_description = "Main Image Preview"

#     # ==============================
#     # 🔹 Background Image Preview
#     # ==============================
#     def bg_image_preview(self, obj):
#         if hasattr(obj, 'bg') and obj.bg:
#             delete_url = reverse('admin:services_service_delete_bg', args=[obj.id])
#             return format_html(
#                 '''
#                 <div style="border:1px solid #ccc; border-radius:8px; padding:4px; display:inline-block; text-align:center;">
#                     <img src="{}" style="width:50px; height:auto; border-radius:6px; box-shadow:0 0 5px rgba(0,0,0,0.1);" />
#                 </div>
#                 ''',
#                 obj.bg.url,
#                 delete_url,
#             )
#         return format_html('<span style="color:#999;">No background image uploaded</span>')
#     bg_image_preview.short_description = "Background Image Preview"

#     # ==============================
#     # 🔹 Edit/Delete links
#     # ==============================
#     def edit_link(self, obj):
#         return format_html(
#             '<a href="/admin/services/services/{}/change/" style="color:#0066cc;">✏ Edit</a>', obj.id
#         )
#     edit_link.short_description = "Edit"

#     def delete_link(self, obj):
#         return format_html(
#             '<a href="/admin/services/services/{}/delete/" style="color:#d00;">🗑 Delete</a>', obj.id
#         )
#     delete_link.short_description = "Delete"


admin.site.register(ServicePageTopBar)
admin.site.register(Service)
admin.site.register(Categories)
admin.site.register(Faq)
admin.site.register(FaqItem)
admin.site.register(ServiceItemMain)
admin.site.register(ServiceItem)
admin.site.register(ServicesIncludeTopTitle)
admin.site.register(ServicesIncludeTopItem)
admin.site.register(ServicesIncludeBottomTitle)
admin.site.register(ServicesIncludeBottomItem)
