#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from success_stories.models import (
    SuccessStorieTopBar,
    SuccessStorieCategory,
    SuccessStorie,
    SeoTag,
    Schema,
)

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

# =========== Schema Admin =============
class SchemaAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "name",
        "url",
        "created_at",
        "updated_at",
        "action_buttons",
    )
    list_display_links = ("name",)

    list_filter = ("type", "created_at", "updated_at")

    search_fields = (
        "type",
        "name",
        "url",
        "email",
        "phone_number",
    )

    list_per_page = 25

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Basic Info"), {
            "fields": (
                "context",
                "type",
                "name",
                "url",
                "description",
            )
        }),
        (_("Contact Info"), {
            "classes": ("collapse",),
            "fields": (
                "contact_type",
                "email",
                "phone_number",
                "address",
                "logo",
            )
        }),
        (_("Social Profiles (sameAs)"), {
            "classes": ("collapse",),
            "fields": (
                "same_as_facebook",
                "same_as_instagram",
                "same_as_linkedin",
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

class SuccessStorieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "client_name",
        "created_at",
        "get_categories",
        "action_buttons",
    ]

    search_fields = ["title", "client_name", "content", "seo_title", "seo_description"]
    list_filter = ["created_at", "categories"]
    ordering = ["-created_at"]

    readonly_fields = ("created_at",)

    fieldsets = (
        ("Success Story Information", {
            "fields": ("image", "title", "slug", "short_description", "budget_description", "content", "categories")
        }),
        ("Client Information", {
            "fields": ("client_name", "subject", "budget", "duration")
        }),
        ("SEO Meta Information", {
            "classes": ("collapse",),
            "fields": ("seo_title", "seo_description", "seo_keywords")
        }),
        ("Open Graph (OG) Information", {
            "classes": ("collapse",),
            "fields": ("og_title", "og_description", "og_image", "og_image_file", "og_type")
        }),
        ("Twitter Card Information", {
            "classes": ("collapse",),
            "fields": ("twitter_title", "twitter_description", "twitter_image")
        }),
        ("Schema Information", {
            "classes": ("collapse",),
            "fields": ("schema_type", "schema_context", "schema_custom_json")
        }),
        ("System Information", {
            "fields": ("created_at",),
        }),
    )

    def get_categories(self, obj):
        return ", ".join(category.name for category in obj.categories.all())

    get_categories.short_description = "Categories"

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:5px 10px; background:#3c8dbc; color:white; '
            'border-radius:4px; margin-right:6px;">Edit</a>'
            '<a href="{}" style="padding:5px 10px; background:#dd4b39; color:white; '
            'border-radius:4px;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = "Actions"

class SuccessStorieTopBarAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "action_buttons"]
    search_fields = ["title", "description"]
    ordering = ["title"]

    fieldsets = (
        ("Top Bar Information", {
            "fields": ("title", "description")
        }),
    )

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:5px 10px; background:#3c8dbc; color:white; '
            'border-radius:4px; margin-right:6px;">Edit</a>'
            '<a href="{}" style="padding:5px 10px; background:#dd4b39; color:white; '
            'border-radius:4px;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = "Actions"

class SuccessStorieCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "action_buttons"]
    search_fields = ["name"]
    ordering = ["name"]

    fieldsets = (
        ("Category Information", {
            "fields": ("name",)
        }),
    )

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:5px 10px; background:#3c8dbc; color:white; '
            'border-radius:4px; margin-right:6px;">Edit</a>'
            '<a href="{}" style="padding:5px 10px; background:#dd4b39; color:white; '
            'border-radius:4px;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = "Actions"

# REGISTER MODELS HERE.
admin.site.register(SuccessStorieTopBar, SuccessStorieTopBarAdmin)
admin.site.register(SuccessStorieCategory, SuccessStorieCategoryAdmin)
admin.site.register(SuccessStorie, SuccessStorieAdmin)
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
