from django.contrib import admin
from pages.models import Page, SeoTag, Schema, Organization

# Register your models here.
class SeoTagInline(admin.StackedInline):
    model = SeoTag
    extra = 0
    max_num = 1
    can_delete = True

    fieldsets = (
        ("Basic SEO", {
            "fields": (
                "title",
                "description",
                "keywords",
                "author",
            )
        }),
        ("Open Graph", {
            "classes": ("collapse",),
            "fields": (
                "og_title",
                "og_description",
                "og_image",
                "og_image_file",
                "og_url",
                "og_type",
                "og_locale",
                "og_site_name",
            )
        }),
        ("Twitter Card", {
            "classes": ("collapse",),
            "fields": (
                "twitter_card",
                "twitter_site",
                "twitter_creator",
                "twitter_title",
                "twitter_description",
                "twitter_image",
            )
        }),
        ("Extra SEO", {
            "classes": ("collapse",),
            "fields": (
                "canonical_url",
                "category",
                "creator",
                "published_time",
                "modified_time",
            )
        }),
    )

class SchemaInline(admin.StackedInline):
    model = Schema
    extra = 0
    max_num = 1
    can_delete = True

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SeoTagInline, SchemaInline]

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    search_fields = ("name",)
    readonly_fields = ()

@admin.register(SeoTag)
class SeoTagAdmin(admin.ModelAdmin):
    list_display = ("page", "title", "created_at")
    search_fields = ("page__name", "title")

@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_display = ("page", "url")
    search_fields = ("page__name", "url")
