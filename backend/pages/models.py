####################################################
"""
PAGES MODELS HERE.
"""
####################################################
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# CREATE MODELS HERE.

# =========== PAGES =============
class Pages(models.Model):
    name = models.CharField(
        unique=True,
        max_length=180,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Page Name'),
        help_text=_('Enter your website page name...'),
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        max_length=180,
        verbose_name=_('Page Slug'),
    )
    content = RichTextField(
        verbose_name=_('Page description'),
        help_text=_('Enter your website page content...'),
    )
    seo_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('SEO Title'),
        help_text=_('SEO Title of the page for search engines'),
    )
    seo_keywords = models.ManyToManyField(
        'SEOKeyword',
        blank=True,
        related_name='pages',
        verbose_name=_('SEO Keywords'),
        help_text=_('Keywords related to this page for SEO'),
    )
    seo_description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('SEO Description'),
        help_text=_('SEO description of the page for search engines'),
    )
    seo_canonical = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Canonical URL'),
        help_text=_('Canonical URL to avoid duplicate content'),
    )
    seo_author = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Author'),
        help_text=_('Author name for SEO purposes'),
    )

    def save(self, *args, **kwargs):
        if self.name.lower() == 'home':
            self.slug = '/'
        elif self.slug == '/':
            raise ValidationError("The slug '/' is reserved for the Home page.")
        
        super(Pages, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# ============ SEO KEYWORDS ============
class SEOKeyword(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Keyword'),
        help_text=_('SEO keyword or phrase'),
    )

    def __str__(self):
        return self.name

# =========== OPEN GRAPH META TAGS ==============
class OpenGraphMetaTags(models.Model):
    page = models.OneToOneField(
        Pages,
        related_name='og_meta',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('OG Title'),
        help_text=_('Open Graph Title for social media'),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('OG Description'),
        help_text=_('Open Graph Description for social media'),
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('OG URL'),
        help_text=_('URL for Open Graph sharing'),
    )
    type = models.CharField(
        max_length=50,
        default='website',
        verbose_name=_('OG Type'),
        help_text=_('Open Graph Type (e.g., website, article)'),
    )
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('OG Image'),
        help_text=_('Image URL for Open Graph sharing'),
    )
    locale = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_('OG Locale'),
        help_text=_('Open Graph Locale (e.g., en_US)'),
    )
    site_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('OG Site Name'),
        help_text=_('Open Graph Site Name'),
    )
    audio = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('OG Audio'),
        help_text=_('Audio URL for Open Graph'),
    )
    video = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('OG Video'),
        help_text=_('Video URL for Open Graph'),
    )
    secure_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('OG Secure URL'),
        help_text=_('Secure URL for Open Graph'),
    )
    image_width = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('OG Image Width'),
        help_text=_('Open Graph Image Width'),
    )
    image_height = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('OG Image Height'),
        help_text=_('Open Graph Image Height'),
    )
    determiner = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('OG Determiner'),
        help_text=_('Open Graph Determiner (e.g., the, a, an)'),
    )

    def __str__(self):
        return f"Open Graph Meta for {self.page.name}"

# =========== TWITTER CARDMETA TAGS ==============
class TwitterCardMetaTags(models.Model):
    page = models.OneToOneField(
        Pages,
        related_name='twitter_meta',
        on_delete=models.CASCADE,
    )
    card_type = models.CharField(
        max_length=20,
        default='summary_large_image',
        verbose_name=_('Twitter Card Type'),
        help_text=_('Type of Twitter Card (summary, summary_large_image, etc.)'),
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Twitter Card Title'),
        help_text=_('Title for Twitter Card'),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Twitter Card Description'),
        help_text=_('Description for Twitter Card'),
    )
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Twitter Card Image'),
        help_text=_('Image URL for Twitter Card'),
    )
    site = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Twitter Site Handle'),
        help_text=_('Twitter site handle (e.g., @YourSiteHandle)'),
    )
    creator = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Twitter Creator Handle'),
        help_text=_('Twitter creator handle (e.g., @CreatorHandle)'),
    )

    def __str__(self):
        return f"Twitter Card Meta for {self.page.name}"

# =========== ADDITIONAL SEO FIELDS ==============
class AdditionalSEOFields(models.Model):
    page = models.OneToOneField(
        Pages,
        related_name='additional_seo',
        on_delete=models.CASCADE,
    )
    json_ld_schema = models.JSONField(
        blank=True,
        null=True,
        verbose_name=_('JSON-LD Schema'),
        help_text=_('Structured data in JSON-LD format for SEO'),
    )
    robots_txt = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Robots.txt'),
        help_text=_('Custom robots.txt content for SEO'),
    )

    def __str__(self):
        return f"Additional SEO Fields for {self.page.name}"
