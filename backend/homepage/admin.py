#########################################
"""
ADMIN UI DESIGN SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from homepage.models import (
    Banner,
    PaymnetInfo,
    SecurityFirm, 
    CybersecuritySolutionTitle, 
    CybersecuritySolutionItem,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    ReviewTopBar,
    Review,
    ExperienceEic,
    ExperienceEicItem,
    GloballyAccredited,
    SeoTag,
    Organization,
    HomePageSchema,
    Rasel,
)
from django import forms
from django.db import models

class OrganizationInline(admin.StackedInline):
    model = Organization
    extra = 0
    max_num = 1

# ========== SEO TAG TOP BAR ADMIN ==========
class SeoTagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "og_type",
        "created_at",
        "updated_at",
        "action_buttons",
    )
    list_display_links = ("title",)
    list_filter = ("og_type", "created_at", "updated_at")
    search_fields = (
        "title",
        "description",
        "keywords",
        "og_title",
        "twitter_title",
    )
    list_per_page = 25
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Basic SEO"), {
            "fields": (
                "title",
                "description",
                "keywords",
            )
        }),
        (_("Open Graph (Facebook / LinkedIn)"), {
            "classes": ("collapse",),
            "fields": (
                "og_title",
                "og_description",
                "og_image",
                "og_image_file",
                "og_url",
                "og_type",
            )
        }),
        (_("Twitter Card"), {
            "classes": ("collapse",),
            "fields": (
                "twitter_title",
                "twitter_description",
                "twitter_image",
            )
        }),
        (_("System Info"), {
            "classes": ("collapse",),
            "fields": ("created_at", "updated_at"),
        }),
    )

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" '
            'style="padding:4px 8px; background:#4caf50; color:white; border-radius:4px; text-decoration:none; margin-right:4px;">Edit</a>'
            '<a href="{}" '
            'style="padding:4px 8px; background:#f44336; color:white; border-radius:4px; text-decoration:none;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = _("Actions")
    action_buttons.allow_tags = True

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


@admin.register(HomePageSchema)
class HomePageSchemaAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]

    list_display = ("name", "url")
    fieldsets = (
        ("Homepage Info", {
            "fields": ("name", "url", "description")
        }),
    )
admin.site.register(Rasel)
admin.site.register(Banner)
admin.site.register(PaymnetInfo)
admin.site.register(SecurityFirm, SecurityFirmAdmin)
admin.site.register(CybersecuritySolutionTitle)
admin.site.register(CybersecuritySolutionItem)
admin.site.register(OurProvenProcessSecurity)
admin.site.register(OurProvenProcessSecurityItems)
admin.site.register(ReviewTopBar)
admin.site.register(Review)
admin.site.register(ExperienceEic)
admin.site.register(ExperienceEicItem)
admin.site.register(GloballyAccredited)
admin.site.register(SeoTag, SeoTagAdmin)
