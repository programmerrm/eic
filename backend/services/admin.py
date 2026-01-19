# #########################################
# """
# ADMIN UI DESIGN SETUP
# """
# #########################################
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from services.models import (
    SeoTag,
    ServicePageTopBar, 
    Service, 
    Categories, 
    Faq, 
    FaqItem, 
    ServiceItemMain, 
    ServiceItem, 
    ServicesIncludeTopTitle, 
    ServicesIncludeTopItem, 
    ServicesIncludeBottomTitle, 
    ServicesIncludeBottomItem,
    ComplianceTitle,
    ComplianceItemList,
    ComplianceItem,
    ServicePaymnet, 
    ServiceWhyChooseUsTitle, 
    ServiceWhyChooseUsItem,
    ServicePageSchema,
    Organization,
)

class OrganizationInline(admin.StackedInline):
    model = Organization
    extra = 0
    max_num = 1

@admin.register(ServicePageSchema)
class ServicePageSchemaAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]

    list_display = ("name", "url")
    fieldsets = (
        ("ServicePage Info", {
            "fields": ("name", "url", "description")
        }),
    )

class ServicePageTopBarAdmin(admin.ModelAdmin):
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

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "get_categories",
        "action_buttons",
    ]
    search_fields = ["title", "description", "seo_title", "seo_description"]
    list_filter = ["categories"]
    ordering = ["-title"]

    readonly_fields = ("slug",)

    fieldsets = (
        ("Service Information", {
            "fields": ("image", "title", "slug", "description", "categories")
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

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "action_buttons"]
    search_fields = ["name"]
    ordering = ["-name"]

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

class FaqAdmin(admin.ModelAdmin):
    list_display = ["title", "service", "action_buttons"]
    search_fields = ["title", "service__title"]
    list_filter = ["service"]
    ordering = ["-title"]

    fieldsets = (
        ("FAQ Information", {
            "fields": ("service", "title", "image")
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

class FaqItemAdmin(admin.ModelAdmin):
    list_display = ["question", "service", "action_buttons"]
    search_fields = ["question", "service__title"]
    list_filter = ["service"]
    ordering = ["-question"]

    fieldsets = (
        ("FAQ Item Information", {
            "fields": ("service", "question", "answer")
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

class ServiceItemMainAdmin(admin.ModelAdmin):
    list_display = ["service", "normal_title", "span_title", "action_buttons"]
    search_fields = ["normal_title", "span_title", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Service Information", {
            "fields": ("service", "normal_title", "span_title")
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

class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ["service", "title", "description", "action_buttons"]
    search_fields = ["title", "description", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Service Item Information", {
            "fields": ("service", "image", "title", "description")
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

class ServicesIncludeTopTitleAdmin(admin.ModelAdmin):
    list_display = ["service", "title", "action_buttons"]
    search_fields = ["title", "service__title"]
    ordering = ["service"]

    fieldsets = (
        ("Service Include Top Title Information", {
            "fields": ("service", "title", "description")
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

class ServicesIncludeTopItemAdmin(admin.ModelAdmin):
    list_display = ["service", "title", "description", "action_buttons"]
    search_fields = ["title", "description", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Service Include Top Item Information", {
            "fields": ("service", "image", "title", "description")
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

class ServicesIncludeBottomTitleAdmin(admin.ModelAdmin):
    list_display = ["service", "title", "description", "action_buttons"]
    search_fields = ["title", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Bottom Title Information", {
            "fields": ("service", "title", "description")
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

class ServicesIncludeBottomItemAdmin(admin.ModelAdmin):
    list_display = ["service", "title", "description", "action_buttons"]
    search_fields = ["title", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Bottom Item Information", {
            "fields": ("service", "title", "description")
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

class ComplianceTitleAdmin(admin.ModelAdmin):
    list_display = ["service", "title_before_span", 'title_span', 'title_after_span', "btn_name", "action_buttons"]
    search_fields = ["title_span", "btn_name", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Service Compliance Title", {
            "fields": ("service", "title_before_span", 'title_span', 'title_after_span', "btn_name", "btn_url")
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

class ComplianceItemListAdmin(admin.ModelAdmin):
    list_display = ["name", "action_buttons"]
    search_fields = ["name",]

    fieldsets = (
        ("Service Compliance List", {
            "fields": ( "name", "items")
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

class ComplianceItemAdmin(admin.ModelAdmin):
    list_display = ["title", "action_buttons"]
    search_fields = ["title",]

    fieldsets = (
        ("Service Compliance Item", {
            "fields": ("service", "title", 'image')
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

class ServicePaymnetAdmin(admin.ModelAdmin):
    list_display = ["service", "title_span", "btn_name", "action_buttons"]
    search_fields = ["title_span", "btn_name", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Service Payment Information", {
            "fields": ("service", "image", "title_before_span", "title_span", "title_after_span", "description", "btn_name", "btn_url")
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

class ServiceWhyChooseUsTitleAdmin(admin.ModelAdmin):
    list_display = ["service", "title_before_span", "title_span", "title_after_span", "action_buttons"]
    search_fields = ["title_before_span", "title_span", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Why Choose Us Title Information", {
            "fields": ("service", "title_before_span", "title_span", "title_after_span", "image")
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

class ServiceWhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = ["service", "name", "action_buttons"]
    search_fields = ["name", "service__title"]
    list_filter = ["service"]
    ordering = ["service"]

    fieldsets = (
        ("Why Choose Us Item Information", {
            "fields": ("service", "name")
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
admin.site.register(SeoTag)
admin.site.register(ServicePageTopBar, ServicePageTopBarAdmin)
admin.site.register(Service)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(FaqItem, FaqItemAdmin)
admin.site.register(ServiceItemMain, ServiceItemMainAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(ServicesIncludeTopTitle, ServicesIncludeTopTitleAdmin)
admin.site.register(ServicesIncludeTopItem, ServicesIncludeTopItemAdmin)
admin.site.register(ServicesIncludeBottomTitle, ServicesIncludeBottomTitleAdmin)
admin.site.register(ServicesIncludeBottomItem, ServicesIncludeBottomItemAdmin)
admin.site.register(ComplianceTitle, ComplianceTitleAdmin)
admin.site.register(ComplianceItemList, ComplianceItemListAdmin)
admin.site.register(ComplianceItem, ComplianceItemAdmin)
admin.site.register(ServicePaymnet, ServicePaymnetAdmin)
admin.site.register(ServiceWhyChooseUsTitle, ServiceWhyChooseUsTitleAdmin)
admin.site.register(ServiceWhyChooseUsItem, ServiceWhyChooseUsItemAdmin)
