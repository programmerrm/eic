#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from blogs.models import BlogTopBar, Blog, Tag, SeoTag, Schema

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

class BlogTopBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', "action_buttons"]

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:5px 10px; background:#3c8dbc; color:white; '
            'border-radius:4px; margin-right:5px;">Edit</a>'
            '<a href="{}" style="padding:5px 10px; background:#dd4b39; color:white; '
            'border-radius:4px;">Delete</a>',
            change_url,
            delete_url
        )

    action_buttons.short_description = "Actions"

class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "action_buttons"]
    search_fields = ["name"]
    ordering = ["name"]

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:5px 10px; background:#3c8dbc; color:white; '
            'border-radius:4px; margin-right:5px;">Edit</a>'
            '<a href="{}" style="padding:5px 10px; background:#dd4b39; color:white; '
            'border-radius:4px;">Delete</a>',
            change_url,
            delete_url
        )

    action_buttons.short_description = "Actions"

class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author_name",
        "created_at",
        "get_tags",
        "action_buttons",
    ]

    search_fields = ["title", "author_name", "content"]
    list_filter = ["created_at", "tags"]
    ordering = ["-created_at"]

    readonly_fields = ("slug", "created_at")

    fieldsets = (
        ("Blog Information", {
            "fields": ("image", "title", "slug", "content", "tags")
        }),
        ("Author Details", {
            "fields": ("author_image", "author_name", "author_bio", "author_description")
        }),
        ("Author Social Links", {
            "fields": (
                "author_facebook_url",
                "author_twitter_url",
                "author_medium_url",
            )
        }),
        ("SEO Information", {
            "classes": ("collapse",),
            "fields": ("seo_tag",)
        }),
        ("Schema Information", {
            "classes": ("collapse",),
            "fields": ("schema",)
        }),
        ("System Information", {
            "fields": ("created_at",),
        }),
    )

    def get_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    get_tags.short_description = "Tags"

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
admin.site.register(BlogTopBar, BlogTopBarAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
