#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from blogs.models import BlogTopBar, Blog, Tag

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

    search_fields = ["title", "author_name", "content", "seo_title", "seo_description"]
    list_filter = ["created_at", "tags"]
    ordering = ["-created_at"]

    readonly_fields = ("created_at",)

    fieldsets = (
        ("Blog Information", {
            "fields": ("image", "title", "content", "tags")
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
        ("SEO Meta Information", {
            "classes": ("collapse",),
            "fields": (
                "seo_title",
                "seo_description",
                "seo_keywords",
            )
        }),
        ("Open Graph (OG) Information", {
            "classes": ("collapse",),
            "fields": (
                "og_title",
                "og_description",
                "og_image",
                "og_image_file",
                "og_type",
            )
        }),
        ("Twitter Card Information", {
            "classes": ("collapse",),
            "fields": (
                "twitter_title",
                "twitter_description",
                "twitter_image",
            )
        }),
        ("Schema Information", {
            "classes": ("collapse",),
            "fields": (
                "schema_type",
                "schema_context",
                "schema_custom_json",
            )
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
