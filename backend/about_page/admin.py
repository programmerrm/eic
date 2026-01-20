from django.contrib import admin
from about_page.models import AboutTopBar, SecureFutureTopBar, SecureFutureItem, SecurityFirm, DigitalSecuritySolutionTopBar, DigitalSecuritySolutionItem, HappyJourneyTopBar, HappyJourneyItem,SeoTag, AboutPageSchema, Organization

class OrganizationInline(admin.StackedInline):
    model = Organization
    extra = 0
    max_num = 1

@admin.register(AboutPageSchema)
class AboutPageSchemaAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]

    list_display = ("name", "url")
    fieldsets = (
        ("Aboutpage Info", {
            "fields": ("name", "url", "description")
        }),
    )
    
admin.site.register(SeoTag)

# Register your models here.
admin.site.register(AboutTopBar)
admin.site.register(SecureFutureTopBar)
admin.site.register(SecureFutureItem)
admin.site.register(SecurityFirm)
admin.site.register(DigitalSecuritySolutionTopBar)
admin.site.register(DigitalSecuritySolutionItem)
admin.site.register(HappyJourneyTopBar)
admin.site.register(HappyJourneyItem)
