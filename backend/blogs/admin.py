#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from blogs.models import BlogTopBar, Blog, Tag, SeoTag, Schema

class SeoTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

class SchemaAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'url', 'contact_type', 'email', 'phone_number', 'created_at', 'updated_at')

class BlogTopBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', "edit_button", "delete_button"]

    def edit_button(self, obj):
        url = reverse("admin:blogs_tag_change", args=[obj.id])
        return format_html(f'<a class="button" style="padding:5px 10px; background:#3c8dbc; color:white; border-radius:4px;" href="{url}">Edit</a>')
    edit_button.short_description = "Edit"

    def delete_button(self, obj):
        url = reverse("admin:blogs_tag_delete", args=[obj.id])
        return format_html(f'<a class="button" style="padding:5px 10px; background:#dd4b39; color:white; border-radius:4px;" href="{url}">Delete</a>')
    delete_button.short_description = "Delete"

class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "edit_button", "delete_button"]
    search_fields = ["name"]
    ordering = ["name"]

    def edit_button(self, obj):
        url = reverse("admin:blogs_tag_change", args=[obj.id])
        return format_html(f'<a class="button" style="padding:5px 10px; background:#3c8dbc; color:white; border-radius:4px;" href="{url}">Edit</a>')
    edit_button.short_description = "Edit"

    def delete_button(self, obj):
        url = reverse("admin:blogs_tag_delete", args=[obj.id])
        return format_html(f'<a class="button" style="padding:5px 10px; background:#dd4b39; color:white; border-radius:4px;" href="{url}">Delete</a>')
    delete_button.short_description = "Delete"

class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author_name",
        "created_at",
        "get_tags",
        "edit_button",
        "delete_button",
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
        ("System Information", {
            "fields": ("created_at",),
        }),
    )

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "Tags"

    def edit_button(self, obj):
        url = reverse("admin:blogs_blog_change", args=[obj.id])
        return format_html(
            '<a class="button" style="padding:5px 10px; background:#3c8dbc; '
            'color:white; border-radius:4px;" href="{}">Edit</a>', url)
    edit_button.short_description = "Edit"

    def delete_button(self, obj):
        url = reverse("admin:blogs_blog_delete", args=[obj.id])
        return format_html(
            '<a class="button" style="padding:5px 10px; background:#dd4b39; '
            'color:white; border-radius:4px;" href="{}">Delete</a>', url)
    delete_button.short_description = "Delete"

# REGISTER MODELS HERE.
admin.site.register(BlogTopBar, BlogTopBarAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
