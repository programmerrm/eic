from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.db import models
from features.models import Feature, FeatureItem
import os


#########################################
# FEATURE ADMIN
#########################################
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'styled_title',
        'features_btn_name',
        'features_btn_url',
        'edit_link',
        'delete_link',
    )

    fieldsets = (
        ('Feature Title Section', {
            'fields': ('title_before_span', 'title_span', 'title_after_span')
        }),
        ('Feature Button Section', {
            'fields': ('features_btn_name', 'features_btn_url')
        }),
    )

    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={
                'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
            })
        },
        models.TextField: {
            'widget': forms.Textarea(attrs={
                'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
            })
        },
    }

    def styled_title(self, obj):
        return format_html(
            '<div style="border:1px solid #ccc; border-radius:6px; padding:6px; background:#f9f9f9;">{} '
            '<span style="color:#007bff;">{}</span> {}</div>',
            obj.title_before_span or "",
            obj.title_span or "",
            obj.title_after_span or ""
        )
    styled_title.short_description = "Feature Title (Styled)"

    def edit_link(self, obj):
        return format_html(
            '<a href="/admin/features/feature/{}/change/" style="color:#007bff;">✏ Edit</a>',
            obj.id
        )
    edit_link.short_description = "Edit"

    def delete_link(self, obj):
        return format_html(
            '<a href="/admin/features/feature/{}/delete/" style="color:#d00;">🗑 Delete</a>',
            obj.id
        )
    delete_link.short_description = "Delete"


#########################################
# FEATURE ITEM ADMIN
#########################################
@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image_preview',
        'bg_preview',
        'edit_link',
        'delete_link',
    )

    readonly_fields = (
        'slug',
        'image_preview',
        'bg_preview',
    )

    fieldsets = (
        ('Feature Info', {
            'fields': ('name', 'description')
        }),
        ('Images', {
            'fields': ('image', 'image_preview', 'bg', 'bg_preview')
        }),
    )

    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={
                'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
            })
        },
        models.TextField: {
            'widget': forms.Textarea(attrs={
                'style': 'width:100%; border:1px solid #ccc; border-radius:6px; padding:6px;'
            })
        },
    }

    # ---------- IMAGE PREVIEW ----------
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<div style="position:relative; display:inline-block;">'
                '<img src="{}" width="100" style="border-radius:6px; box-shadow:0 0 5px rgba(0,0,0,0.1);" />'
                '</div>',
                obj.image.url, obj.id
            )
        return format_html('<span style="color:#999;">No Image</span>')
    image_preview.short_description = "Image Preview"

    def bg_preview(self, obj):
        if obj.bg:
            return format_html(
                '<div style="position:relative; display:inline-block;">'
                '<img src="{}" width="100" style="border-radius:6px; box-shadow:0 0 5px rgba(0,0,0,0.1);" />'
                '</div>',
                obj.bg.url, obj.id
            )
        return format_html('<span style="color:#999;">No BG Image</span>')
    bg_preview.short_description = "BG Preview"

    # ---------- CUSTOM DELETE HANDLERS ----------
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/delete_image/', self.admin_site.admin_view(self.delete_image), name='delete_image'),
            path('<int:object_id>/delete_bg/', self.admin_site.admin_view(self.delete_bg), name='delete_bg'),
        ]
        return custom_urls + urls

    def delete_image(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj and obj.image:
            if os.path.isfile(obj.image.path):
                os.remove(obj.image.path)
            obj.image = None
            obj.save()
        from django.shortcuts import redirect
        return redirect(f'/admin/features/featureitem/{object_id}/change/')

    def delete_bg(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj and obj.bg:
            if os.path.isfile(obj.bg.path):
                os.remove(obj.bg.path)
            obj.bg = None
            obj.save()
        from django.shortcuts import redirect
        return redirect(f'/admin/features/featureitem/{object_id}/change/')

    def edit_link(self, obj):
        return format_html(
            '<a href="/admin/features/featureitem/{}/change/" style="color:#007bff;">✏ Edit</a>',
            obj.id
        )
    edit_link.short_description = "Edit"

    def delete_link(self, obj):
        return format_html(
            '<a href="/admin/features/featureitem/{}/delete/" style="color:#d00;">🗑 Delete</a>',
            obj.id
        )
    delete_link.short_description = "Delete"

    def save_model(self, request, obj, form, change):
        from django.utils.text import slugify
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
