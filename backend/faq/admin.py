#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from faq.models import FaqTopBar, FaqSection, FaqItem, SeoTag, Schema

class SeoTagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "canonical",
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
        "canonical",
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
                "canonical",
                "robots",
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

class FaqTopBarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_description",
        "action_buttons",
    )
    search_fields = ("title", "description")

    def short_description(self, obj):
        return (obj.description[:60] + "...") if len(obj.description) > 60 else obj.description

    short_description.short_description = "Description"

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

    action_buttons.short_description = "Actions"

class FaqSectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image_preview",
        "action_buttons",
    )
    search_fields = ("title",)

    readonly_fields = ("image_preview",)

    fieldsets = (
        ("FAQ Section Info", {
            "fields": ("title", "image", "image_preview")
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:60px; border-radius:4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Image"

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

    action_buttons.short_description = "Actions"

class FaqItemAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "short_answer",
        "action_buttons",
    )
    search_fields = ("question", "answer")

    def short_answer(self, obj):
        return (obj.answer[:60] + "...") if len(obj.answer) > 60 else obj.answer

    short_answer.short_description = "Answer"

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

    action_buttons.short_description = "Actions"

# REGISTER MODELS HERE.
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
admin.site.register(FaqTopBar, FaqTopBarAdmin)
admin.site.register(FaqSection, FaqSectionAdmin)
admin.site.register(FaqItem, FaqItemAdmin)
