#########################################
"""
ADMIN UI DESIGN SETUP
"""
#########################################
from django.contrib import admin, messages
from django.utils.html import format_html
from django.urls import path, reverse
from django.shortcuts import redirect
from django.shortcuts import redirect, get_object_or_404
from homepage.models import (
    Banner,
    PaymnetInfo,
    SecurityFirm, 
    CybersecuritySolutionTitle, 
    CybersecuritySolutionItem,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems
)
from django import forms
from django.db import models


# class BannerAdmin(admin.ModelAdmin):
#     list_display = (
#         'styled_title',
#         'styled_sub_title',
#         'video_preview',
#         'payment_logo_preview',
#         'edit_link',
#         'delete_link',
#     )

#     readonly_fields = (
#         'video_preview',
#         'payment_logo_preview',
#     )

#     fieldsets = (
#         ('Banner Info', {
#             'fields': ('video_file', 'video_preview', 'title', 'sub_title', 'description', 'short_description')
#         }),
#         ('Payment Section', {
#             'fields': ('payment_logo', 'payment_logo_preview')
#         }),
#         ('Get Started Button', {
#             'fields': ('get_started_name', 'get_started_url')
#         }),
#         ('Secure My Business Button', {
#             'fields': ('secure_business_name', 'secure_business_url')
#         }),
#         ('Company Profile Button', {
#             'fields': ('company_profile_name', 'company_profile_url')
#         }),
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

#     # 🗑 Custom delete handlers
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path(
#                 '<int:banner_id>/delete-video/',
#                 self.admin_site.admin_view(self.delete_video_view),
#                 name='homepage_banner_delete_video',
#             ),
#             path(
#                 '<int:banner_id>/delete-logo/',
#                 self.admin_site.admin_view(self.delete_logo_view),
#                 name='homepage_banner_delete_logo',
#             ),
#         ]
#         return custom_urls + urls

#     def delete_video_view(self, request, banner_id):
#         banner = Banner.objects.get(pk=banner_id)
#         if banner.video_file:
#             banner.video_file.delete(save=False)
#             banner.video_file = None
#             banner.save()
#             self.message_user(request, "Video deleted successfully.", messages.SUCCESS)
#         else:
#             self.message_user(request, "No video to delete.", messages.WARNING)
#         return redirect(reverse('admin:homepage_banner_change', args=[banner_id]))

#     def delete_logo_view(self, request, banner_id):
#         banner = Banner.objects.get(pk=banner_id)
#         if banner.payment_logo:
#             banner.payment_logo.delete(save=False)
#             banner.payment_logo = None
#             banner.save()
#             self.message_user(request, "Payment logo deleted successfully.", messages.SUCCESS)
#         else:
#             self.message_user(request, "No payment logo to delete.", messages.WARNING)
#         return redirect(reverse('admin:homepage_banner_change', args=[banner_id]))

#     # 🖋 Styled display columns
#     def styled_title(self, obj):
#         return format_html(
#             '<div style="border:1px solid #ccc; border-radius:6px; padding:6px; background:#f9f9f9;">{}</div>',
#             obj.title or "No Title"
#         )
#     styled_title.short_description = "Title"

#     def styled_sub_title(self, obj):
#         return format_html(
#             '<div style="border:1px solid #ddd; border-radius:6px; padding:6px; background:#fcfcfc;">{}</div>',
#             obj.sub_title or "No Sub Title"
#         )
#     styled_sub_title.short_description = "Sub Title"

#     # 🎬 Video preview
#     def video_preview(self, obj):
#         if obj.video_file:
#             delete_url = reverse('admin:homepage_banner_delete_video', args=[obj.id])
#             return format_html(
#                 '''
#                 <div style="border:1px solid #ccc; border-radius:8px; padding:6px; text-align:center; background:#fafafa;">
#                     <video width="300" controls style="border-radius:6px;">
#                         <source src="{}" type="video/mp4">
#                         Your browser does not support video playback.
#                     </video>
#                 </div>
#                 ''',
#                 obj.video_file.url,
#                 delete_url
#             )
#         return format_html('<span style="color:#999;">No video uploaded</span>')
#     video_preview.short_description = "Video Preview"

#     # 🖼 Payment logo preview
#     def payment_logo_preview(self, obj):
#         if obj.payment_logo:
#             delete_url = reverse('admin:homepage_banner_delete_logo', args=[obj.id])
#             return format_html(
#                 '''
#                 <div style="border:1px solid #ccc; border-radius:8px; padding:6px; display:inline-block; text-align:center; background:#fafafa;">
#                     <img src="{}" width="150" style="border-radius:6px; box-shadow:0 0 5px rgba(0,0,0,0.1);" />
#                 </div>
#                 ''',
#                 obj.payment_logo.url,
#                 delete_url
#             )
#         return format_html('<span style="color:#999;">No logo uploaded</span>')
#     payment_logo_preview.short_description = "Payment Logo Preview"

#     # ✏ Edit / 🗑 Delete links (in list)
#     def edit_link(self, obj):
#         return format_html(
#             '<a href="/admin/homepage/banner/{}/change/" style="color:#0066cc;">✏ Edit</a>', obj.id
#         )
#     edit_link.short_description = "Edit"

#     def delete_link(self, obj):
#         return format_html(
#             '<a href="/admin/homepage/banner/{}/delete/" style="color:#d00;">🗑 Delete</a>', obj.id
#         )
#     delete_link.short_description = "Delete"


class SecurityFirmAdmin(admin.ModelAdmin):
    list_display = (
        'styled_title',
        'bg_preview',
        'main_img_preview',
        'sub_img_preview',
        'edit_link',
        'delete_link',
    )

    readonly_fields = (
        'bg_preview',
        'main_img_preview',
        'sub_img_preview',
    )

    fieldsets = (
        ('Security Firm Info', {
            'fields': (
                'bg',
                'bg_preview',
                'title_span',
                'title_normal',
                'main_img',
                'main_img_preview',
                'sub_img',
                'sub_img_preview',
            )
        }),
        ('Mission & Vision', {
            'fields': (
                'mission_title',
                'mission_description',
                'vision_title',
                'vision_description',
            )
        }),
        ('Buttons', {
            'fields': (
                'get_to_know_us_btn_name',
                'get_to_know_us_btn_url',
            )
        }),
        ('Statistics', {
            'fields': (
                'security_persentences',
                'response_persentences',
                'compliance_persentences',
            )
        }),
    )

    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(
                attrs={
                    'style': 'width:100%; border:1px solid #ccc; '
                             'border-radius:6px; padding:6px;'
                }
            )
        },
        models.TextField: {
            'widget': forms.Textarea(
                attrs={
                    'style': 'width:100%; border:1px solid #ccc; '
                             'border-radius:6px; padding:6px;'
                }
            )
        },
    }

    def styled_title(self, obj):
        span_part = obj.title_span or ""
        normal_part = obj.title_normal or ""
        return format_html(
            '<div style="border:1px solid #ccc; border-radius:6px; '
            'padding:6px; background:#f9f9f9;">'
            '<span style="color:#2E78AC;">{}</span> {}</div>',
            span_part,
            normal_part,
        )
    styled_title.short_description = "Title"

    def bg_preview(self, obj):
        if obj.bg:
            return format_html(
                '<div style="border:1px solid #ccc; border-radius:6px; '
                'padding:6px; background:#fafafa; text-align:center;">'
                '<img src="{}" width="100"/><br>',
                obj.bg.url,
            )
        return format_html('<span style="color:#999;">No BG uploaded</span>')
    bg_preview.short_description = "Background Preview"

    def main_img_preview(self, obj):
        if obj.main_img:
            return format_html(
                '<div style="border:1px solid #ccc; border-radius:6px; '
                'padding:6px; background:#fafafa; text-align:center;">'
                '<img src="{}" width="100"/><br>',
                obj.main_img.url,
            )
        return format_html(
            '<span style="color:#999;">No main image uploaded</span>'
        )
    main_img_preview.short_description = "Main Image Preview"

    def sub_img_preview(self, obj):
        if obj.sub_img:
            return format_html(
                '<div style="border:1px solid #ccc; border-radius:6px; '
                'padding:6px; background:#fafafa; text-align:center;">'
                '<img src="{}" width="100"/><br>',
                obj.sub_img.url,
            )
        return format_html('<span style="color:#999;">No sub image</span>')
    sub_img_preview.short_description = "Sub Image Preview"

    def edit_link(self, obj):
        url = reverse('admin:homepage_securityfirm_change', args=[obj.id])
        return format_html(
            '<a href="{}" style="color:#0066cc;">✏ Edit</a>',
            url,
        )
    edit_link.short_description = "Edit"

    def delete_link(self, obj):
        url = reverse('admin:homepage_securityfirm_delete', args=[obj.id])
        return format_html(
            '<a href="{}" style="color:#d00;">🗑 Delete</a>',
            url,
        )
    delete_link.short_description = "Delete"

admin.site.register(Banner)
admin.site.register(PaymnetInfo)
admin.site.register(SecurityFirm, SecurityFirmAdmin)
admin.site.register(CybersecuritySolutionTitle)
admin.site.register(CybersecuritySolutionItem)
admin.site.register(OurProvenProcessSecurity)
admin.site.register(OurProvenProcessSecurityItems)
