####################################################
"""
SERVICES MODELS HERE.
"""
####################################################
import json
from django.db import models
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION

# CREATE MODELS HERE.

# ==================== SEO TAGS ====================
class SeoTag(models.Model):
    # Basic SEO
    title = models.CharField(null=True, blank=True, max_length=380)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=280, blank=True, null=True)

     # Open Graph
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    og_image = models.URLField(blank=True, null=True)
    og_image_file = models.ImageField(upload_to="seo/", blank=True, null=True)
    og_url = models.URLField(blank=True, null=True)
    og_type = models.CharField(max_length=50, default="website")
    og_locale = models.CharField(max_length=50, blank=True, null=True)
    og_site_name = models.CharField(max_length=255, blank=True, null=True)

    # Twitter Card
    twitter_card = models.CharField(max_length=50, blank=True, null=True, default="summary_large_image")
    twitter_site = models.CharField(max_length=50, blank=True, null=True)
    twitter_creator = models.CharField(max_length=50, blank=True, null=True)
    twitter_title = models.CharField(max_length=255, blank=True, null=True)
    twitter_description = models.TextField(blank=True, null=True)
    twitter_image = models.URLField(blank=True, null=True)

    # Extra SEO (you can add more if needed)
    canonical_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    published_time = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('SEO Tag')
        verbose_name_plural = _('SEO Tag')

    def __str__(self):
        return "SEO Tag Infomation added"

class ServicePageSchema(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def json_ld(self):
        graph = []

        # Organization
        try:
            org = self.organization
            graph.append(org.schema())
        except Organization.DoesNotExist:
            pass

        # WebSite
        graph.append({
            "@type": "WebSite",
            "@id": f"{self.url}#website",
            "url": self.url,
            "name": self.name,
            "publisher": {
                "@id": f"{self.url}#organization"
            }
        })

        # WebPage (Homepage)
        graph.append({
            "@type": "WebPage",
            "@id": f"{self.url}#homepage",
            "url": self.url,
            "name": self.name,
            "description": self.description,
            "isPartOf": {
                "@id": f"{self.url}#website"
            },
            "about": {
                "@id": f"{self.url}#organization"
            }
        })

        return json.dumps({
            "@context": "https://schema.org",
            "@graph": graph
        }, ensure_ascii=False)

    def __str__(self):
        return f"{self.name} ({self.url})"

class Organization(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField()
    logo = models.URLField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    servicepage_schema = models.OneToOneField(
        ServicePageSchema,
        on_delete=models.CASCADE,
        related_name="organization",
        null=True,
        blank=True
    )

    def schema(self):
        data = {
            "@type": "Organization",
            "@id": f"{self.url}#organization",
            "name": self.name,
            "url": self.url
        }

        if self.logo:
            data["logo"] = {
                "@type": "ImageObject",
                "url": self.logo
            }

        if self.email:
            data["email"] = self.email

        if self.phone_number:
            data["telephone"] = self.phone_number

        same_as = []
        for link in [self.facebook, self.instagram, self.linkedin]:
            if link:
                same_as.append(link)
        if same_as:
            data["sameAs"] = same_as

        return data

    def __str__(self):
        return self.name

# ========== SERVER CATEGORIES ===============
class Categories(models.Model):
    name = models.CharField(
        max_length=280,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name

# ================ SERVICE ==================
class Service(models.Model):
    image = models.FileField(
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
        help_text=_('Upload your service image...'),
    )
    title = models.CharField(
        unique=True,
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    slug = models.SlugField(
        unique=True,
        max_length=280,
        editable=False,
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )
    categories = models.ManyToManyField(
        Categories,
        related_name="services",
        verbose_name=_("Service Categories")
    )

    # ================= SEO FIELDS =================
    seo_title = models.CharField(null=True, blank=True, max_length=380)
    seo_description = models.TextField(null=True, blank=True)
    seo_keywords = models.TextField(blank=True, null=True)
    seo_author = models.CharField(max_length=280, blank=True, null=True)

    # Open Graph
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    og_image = models.URLField(blank=True, null=True)
    og_image_file = models.ImageField(upload_to="seo/", blank=True, null=True)
    og_url = models.URLField(blank=True, null=True)
    og_type = models.CharField(max_length=50, default="website")
    og_locale = models.CharField(max_length=50, blank=True, null=True)
    og_site_name = models.CharField(max_length=255, blank=True, null=True)

    # Twitter Card
    twitter_card = models.CharField(max_length=50, blank=True, null=True, default="summary_large_image")
    twitter_site = models.CharField(max_length=50, blank=True, null=True)
    twitter_creator = models.CharField(max_length=50, blank=True, null=True)
    twitter_title = models.CharField(max_length=255, blank=True, null=True)
    twitter_description = models.TextField(blank=True, null=True)
    twitter_image = models.URLField(blank=True, null=True)

    # Extra SEO
    canonical_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    published_time = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    # ========== SCHEMA INFO ==========
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    schema_description = models.TextField(blank=True, null=True)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="services"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def json_ld(self):
        graph = []

        # Organization
        if self.organization:
            graph.append(self.organization.schema())

        # WebSite
        graph.append({
            "@type": "WebSite",
            "@id": f"{self.url}#website",
            "url": self.url,
            "name": self.name,
            "publisher": {
                "@id": f"{self.url}#organization"
            }
        })

        # WebPage (Service Page)
        graph.append({
            "@type": "WebPage",
            "@id": f"{self.url}#homepage",
            "url": self.url,
            "name": self.name,
            "description": self.schema_description,
            "isPartOf": {
                "@id": f"{self.url}#website"
            },
            "about": {
                "@id": f"{self.url}#organization"
            }
        })

        # Service Schema
        graph.append({
            "@type": "Service",
            "@id": f"{self.url}#service",
            "name": self.title,
            "description": self.seo_description or self.description,
            "provider": {
                "@id": f"{self.organization.url}#organization"
            } if self.organization else None
        })

        return json.dumps({
            "@context": "https://schema.org",
            "@graph": graph
        }, ensure_ascii=False)

    def __str__(self):
        return self.title[:50]

# ========== SERVICE PAGE TOP BAR ============
class ServicePageTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your service page top bar title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service page top bar description...'),
    )

    class Meta:
        verbose_name = _('Service Page Top Bar')
        verbose_name_plural = _('Service Page Top Bar')

    def __str__(self):
        return f"Service page top bar title is {self.title[:50]}"

# =========== Service Item Main =============
class ServiceItemMain(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='main_item',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    normal_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Normal Title'),
        help_text=_('Enter your service main normal title...'),
    )
    span_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Span Title'),
        help_text=_('Enter your service main normal span title...'),
    )

    def __str__(self):
        return f"Service item main infomation added."

# ============== Service Item ================
class ServiceItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='services',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
        help_text=_('Upload your service item image...'),
    )
    title = models.CharField(
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Service item title : {self.title[:50]}"

# ======== Services Include Top Title ===========
class ServicesIncludeTopTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='include_top_title',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Title'),
    )
    description = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = _('Services Include Bottom Title')
        verbose_name_plural = _('Services Include Bottom Title')

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ServicesIncludeTopTitle"

# =========== Services Include Top Item ============
class ServicesIncludeTopItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='include_top_items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='services-include-top/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Title'),
    )
    description = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = _('Services Include Bottom Item')
        verbose_name_plural = _('Services Include Bottom Item')

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ServicesIncludeTopItem"

# ============ Service Why Choose Us Title =============
class ServiceWhyChooseUsTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='service_why_choose_us_title',
        null=True,
        blank=True
    )
    title_before_span = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        default='Default Title',
        verbose_name="Title before span"
    )
    title_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title span'),
    )
    title_after_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title after span'),
    )
    image = models.FileField(
        blank=True, 
        null=True,
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
    )

    def __str__(self):
        return self.title_span[:50]

# ============ Service Why Choose Us Item =============
class ServiceWhyChooseUsItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='service_why_choose_us_item',
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=280,
        verbose_name=_('Name'),
        help_text=_('Enter service item why choose us item name...'),
    )

    def __str__(self):
        return f"Service item why choose us item name : {self.name[:50]}"

# ============== Compliance Title =================
class ComplianceTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='service_compliance_title',
        null=True,
        blank=True
    )
    title_before_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title before span'),
    )
    title_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title span'),
    )
    title_after_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title after span'),
    )
    btn_name = models.CharField(
        max_length=280,
        verbose_name=_('Button Name'),
    )
    btn_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Button URL'),
    )

    class Meta:
        verbose_name = _('Compliance Title')
        verbose_name_plural = _('Compliance Title')

    def __str__(self):
        return "Compliance Title"

# =========== Compliance Item ==============
class ComplianceItem(models.Model):
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        related_name='service_compliance_item',
        null=True,
        blank=True
    )
    image = models.FileField(
        upload_to='compliance/',
        verbose_name=_('Image'),
        null=True,
        blank=True,
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Title'),
    )

    class Meta:
        verbose_name = _('Compliance Item')
        verbose_name_plural = _('Compliance Items')

    def __str__(self):
        return self.title[:50]

# ========== Compliance Item List ===========
class ComplianceItemList(models.Model):
    name = models.CharField(
        max_length=280,
        verbose_name=_('Description'),
    )
    items = models.ManyToManyField(
        ComplianceItem,
        blank=True,
        related_name='lists',
        verbose_name=_('Compliance Items')
    )

    class Meta:
        verbose_name = _('Compliance Item List')
        verbose_name_plural = _('Compliance Lists')

    def __str__(self):
        return self.name[:50]

# ========= Service Paymnet ===========
class ServicePaymnet(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='payment_info',
        null=True,
        blank=True
    )
    image = models.FileField(
        blank=True, 
        null=True,
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Paymnet Image'),
    )
    title_before_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title before span'),
    )
    title_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title span'),
    )
    title_after_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title after span'),
    )
    description = RichTextUploadingField(
        blank=True,
        null=True,
        verbose_name=_('Description'),
    )
    btn_name = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Button Name'),
    )
    btn_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Button URL'),
    )

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_span[:50] or "paymnet"

# ======== Services Include Bottom Title ===========
class ServicesIncludeBottomTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='include_bottom_title',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        blank=True, 
        null=True,
        max_length=280,
        verbose_name=_('Title'),
    )
    description = RichTextUploadingField(
        blank=True, 
        null=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = _('Services Include Top Title')
        verbose_name_plural = _('Services Include Top Title')

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ServicesIncludeBottomTitle"

# =========== Services Include Bottom Item ============
class ServicesIncludeBottomItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='include_bottom_items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        blank=True, 
        null=True,
        max_length=280,
        verbose_name=_('Title'),
    )
    description = RichTextUploadingField(
        blank=True, 
        null=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = _('Services Include Top Item')
        verbose_name_plural = _('Services Include Top Item')

    def save(self, *args, **kwargs):
        if self.description:
            self.description = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ServicesIncludeBottomItem"

# ========== FAQ ==========
class Faq(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='faqs',
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
        help_text=_('Select the service this FAQ belongs to...'),
        null=True,
        blank=True,
    )
    title = models.CharField(
        blank=True, 
        null=True,
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('FAQ Title'),
        help_text=_('Enter your FAQ title...')
    )
    image = models.FileField(
        blank=True, 
        null=True,
        upload_to='faq/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('FAQ File')
    )

    def __str__(self):
        return self.title[:50]

# ========== FAQ ITEM ==========
class FaqItem(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='faq_items',
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
        help_text=_('Select the service this FAQ item belongs to...'),
        blank=True,
        null=True,
    )
    question = models.CharField(
        max_length=280,
        verbose_name=_('Question'),
        help_text=_('Enter your FAQ question...')
    )
    answer = RichTextUploadingField(
        verbose_name=_('Answer'),
        help_text=_('Enter your FAQ answer...')
    )

    def save(self, *args, **kwargs):
        if self.answer:
            self.answer = strip_tags(self.answer)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]
    