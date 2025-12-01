#########################################
"""
ADMIN UI DESIGN SETUP
"""
#########################################
from django.contrib import admin
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.html import format_html
from contact.models import ContactTopBar, ContactForm, ConatctInfomation, GoogleMap, Schema, SeoTag
from django.utils.translation import gettext_lazy as _

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

# ========== CONTACT TOP BAR ADMIN ==========
class ContactTopBarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description_short",
        "image_preview",
        "action_buttons",
    )
    search_fields = ("title",)
    list_filter = ("title",)

    def description_short(self, obj):
        if not obj.description:
            return ""
        return obj.description[:50] + ("..." if len(obj.description) > 50 else "")
    description_short.short_description = "Short Description"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="100" height="100" style="object-fit:cover;"/>'
            )
        return "No Image"
    image_preview.short_description = "Image Preview"

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

# ========== CONTACT FORM ADMIN ==========
class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'company_name',
        'message_short',
        'action_buttons',
    )
    search_fields = ('full_name', 'email', 'company_name')
    list_filter = ('company_name',)

    def message_short(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')
    message_short.short_description = "Short Message"

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:4px 8px; background:#4caf50; '
            'color:white; border-radius:4px; text-decoration:none; margin-right:4px;">Edit</a>'
            '<a href="{}" style="padding:4px 8px; background:#f44336; '
            'color:white; border-radius:4px; text-decoration:none;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = _("Actions")

# ========== CONTACT INFORMATION ADMIN ==========
class ConatctInfomationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'email',
        'address',
        'phone_number1',
        'phone_number2',
        'action_buttons',
    )
    search_fields = ('title', 'email', 'address')
    list_filter = ('title', 'email')

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:4px 8px; background:#4caf50; '
            'color:white; border-radius:4px; text-decoration:none; margin-right:4px;">Edit</a>'
            '<a href="{}" style="padding:4px 8px; background:#f44336; '
            'color:white; border-radius:4px; text-decoration:none;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = _("Actions")

# ========== GOOGLE MAP ADMIN ==========
class GoogleMapAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'action_buttons',
    )
    search_fields = ('url',)
    list_filter = ('url',)

    def action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name

        change_url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.pk])
        delete_url = reverse(f"admin:{app_label}_{model_name}_delete", args=[obj.pk])

        return format_html(
            '<a href="{}" style="padding:4px 8px; background:#4caf50; '
            'color:white; border-radius:4px; text-decoration:none; margin-right:4px;">Edit</a>'
            '<a href="{}" style="padding:4px 8px; background:#f44336; '
            'color:white; border-radius:4px; text-decoration:none;">Delete</a>',
            change_url,
            delete_url,
        )

    action_buttons.short_description = _("Actions")

# REGISTER MODELS HERE
admin.site.register(ContactTopBar, ContactTopBarAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ConatctInfomation, ConatctInfomationAdmin)
admin.site.register(GoogleMap, GoogleMapAdmin)
admin.site.register(SeoTag, SeoTagAdmin)
admin.site.register(Schema, SchemaAdmin)
