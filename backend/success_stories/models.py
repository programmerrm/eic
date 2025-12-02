####################################################
"""
SUCCESS STORIES MODELS HERE.
"""
####################################################
import json
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from ckeditor_uploader.fields import RichTextUploadingField

# ==================== SEO TAGS ====================
class SeoTag(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=380,
        verbose_name=_('SEO Title'),
        help_text=_('The title of the page for search engines and browser tab.')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Meta Description'),
        help_text=_('A short description of the page for SEO purposes.')
    )
    keywords = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Meta Keywords'),
        help_text=_('Comma separated keywords for SEO.')
    )
    og_title = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('OG Title'),
        help_text=_('Title for Open Graph (Facebook, LinkedIn).')
    )
    og_description = models.TextField(
        blank=True, 
        null=True,
        verbose_name=_('OG Description'),
        help_text=_('Description for Open Graph (Facebook, LinkedIn).')
    )
    og_image = models.URLField(
        blank=True, 
        null=True,
        verbose_name=_('OG Image URL'),
        help_text=_('Image URL for Open Graph preview.')
    )
    og_image_file = models.ImageField(
        upload_to="seo/",
        validators=[VALIDATE_IMAGE_EXTENSION],
        blank=True,
        null=True,
        verbose_name=_('OG Image File'),
        help_text=_('Upload OG image instead of or in addition to URL.')
    )
    og_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name=_('OG URL'),
        help_text=_('Canonical URL for Open Graph.')
    )
    og_type = models.CharField(
        max_length=50, 
        default="website",
        verbose_name=_('OG Type'),
        help_text=_('Type of Open Graph object. Default is "website".')
    )
    twitter_title = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Twitter Title'),
        help_text=_('Title for Twitter Card.')
    )
    twitter_description = models.TextField(
        blank=True, 
        null=True,
        verbose_name=_('Twitter Description'),
        help_text=_('Description for Twitter Card.')
    )
    twitter_image = models.URLField(
        blank=True, 
        null=True,
        verbose_name=_('Twitter Image URL'),
        help_text=_('Image URL for Twitter Card preview.')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('SEO Tag')
        verbose_name_plural = _('SEO Tag')

    def __str__(self):
        return self.title or "SEO Infomation added"

# =========== SCHEMA ================
class Schema(models.Model):
    context = models.CharField(
        max_length=280,
        default="https://schema.org",
        verbose_name=_('Context'),
        help_text=_('Always https://schema.org')
    )
    type = models.CharField(
        max_length=50,
        default="CaseStudiesPage",
        verbose_name=_('Type'),
        help_text=_('@type for JSON-LD')
    )
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Page Name'),
        help_text=_('The name/title of the page.')
    )
    url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('URL'),
        help_text=_('Full URL of the page.')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Page description for schema.org.')
    )
    contact_type = models.CharField(
        max_length=280,
        blank=True,
        null=True,
        verbose_name=_('Contact Type'),
        help_text=_('contactType for schema.org, e.g., Customer Support.')
    )
    email = models.EmailField(
        max_length=280,
        blank=True,
        null=True,
        verbose_name=_('Email'),
        help_text=_('Contact email address.')
    )
    phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Phone Number'),
        help_text=_('Contact phone number.')
    )
    logo = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Logo URL'),
        help_text=_('Logo URL for schema.org (recommended).')
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Address'),
        help_text=_('Physical address for local business schema.')
    )
    same_as_facebook = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Facebook Profile'),
        help_text=_('URL to Facebook profile or page.')
    )
    same_as_instagram = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Instagram Profile'),
        help_text=_('URL to Instagram profile.')
    )
    same_as_linkedin = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('LinkedIn Profile'),
        help_text=_('URL to LinkedIn profile.')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('SEO Schema')
        verbose_name_plural = _('SEO Schema')

    def __str__(self):
        return f"{self.type} Schema"

    def json_ld(self):
        data = {
            "@context": self.context,
            "@type": self.type,
            "name": self.name,
            "url": self.url,
            "description": self.description
        }
        if self.contact_type:
            data["contactType"] = self.contact_type
        if self.email:
            data["email"] = self.email
        if self.phone_number:
            data["telephone"] = self.phone_number
        if self.logo:
            data["logo"] = self.logo
        if self.address:
            data["address"] = self.address

        same_as = []
        if self.same_as_facebook:
            same_as.append(self.same_as_facebook)
        if self.same_as_instagram:
            same_as.append(self.same_as_instagram)
        if self.same_as_linkedin:
            same_as.append(self.same_as_linkedin)
        if same_as:
            data["sameAs"] = same_as

        return json.dumps(data, ensure_ascii=False)

# ========= SUCCESS STORIES TOP BAR ===============
class SuccessStorieTopBar(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your case studies top bar title...'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your case studies description...'),
    )

    class Meta:
        verbose_name = _('Case Studies Top Bar')
        verbose_name_plural = _('Case Studies Top Bar')

    def __str__(self):
        return f"Case studies top bar: {self.title[:50]}"

# =========== SUCCESS STORIES CATEGORY ================
class SuccessStorieCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Category Name'),
    )

    def __str__(self):
        return self.name

# ============ SUCCESS STORIES MAIN MODEL==============
class SuccessStorie(models.Model):
    image = models.FileField(
        upload_to='success-stories/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        null=True,
        blank=True,
        verbose_name=_('Image'),
        help_text=_('Upload your success story main image...'),
    )
    title = models.CharField(
        unique=True,
        max_length=280,
        verbose_name=_('Title'),
    )
    slug = models.SlugField(
        editable=False,
        unique=True,
        verbose_name=_('Slug'),
    )
    short_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Short Description'),
    )
    budget_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Budget Description'),
    )
    content = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_('Content'),
    )
    client_name = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Client Name'),
    )
    subject = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Subject'),
    )
    budget = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Budget'),
    )
    duration = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Duration'),
    )

    categories = models.ManyToManyField(
        SuccessStorieCategory,
        related_name='success_stories',
        blank=True,
        verbose_name=_('Categories')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    seo_title = models.CharField(
        max_length=380,
        null=True,
        blank=True,
        verbose_name=_('SEO Title'),
        help_text=_('Custom title for this blog detail page (for browser tab & search engines).'),
    )
    seo_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Meta Description'),
        help_text=_('Short description for this blog (SEO meta description).'),
    )
    seo_keywords = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Meta Keywords'),
        help_text=_('Comma separated keywords for this blog.'),
    )

    og_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('OG Title'),
        help_text=_('Title for Facebook / LinkedIn when this blog is shared.'),
    )
    og_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('OG Description'),
        help_text=_('Description for Open Graph.'),
    )
    og_image = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('OG Image URL'),
        help_text=_('Full URL of image for OG (optional).'),
    )
    og_image_file = models.ImageField(
        upload_to="seo/",
        validators=[VALIDATE_IMAGE_EXTENSION],
        null=True,
        blank=True,
        verbose_name=_('OG Image File'),
        help_text=_('Upload OG image for this blog. If set, this will be used.'),
    )
    og_type = models.CharField(
        max_length=50,
        default="article",
        verbose_name=_('OG Type'),
        help_text=_('Type of Open Graph object, e.g., article.'),
    )

    twitter_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Twitter Title'),
        help_text=_('Title for Twitter card.'),
    )
    twitter_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Twitter Description'),
        help_text=_('Description for Twitter card.'),
    )
    twitter_image = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Twitter Image URL'),
        help_text=_('Image URL for Twitter card preview.'),
    )

    schema_type = models.CharField(
        max_length=50,
        default="BlogPosting",
        null=True,
        blank=True,
        verbose_name=_('Schema Type'),
        help_text=_('JSON-LD @type, e.g., BlogPosting, Article, NewsArticle.'),
    )
    schema_context = models.CharField(
        max_length=280,
        default="https://schema.org",
        null=True,
        blank=True,
        verbose_name=_('Schema Context'),
        help_text=_('Usually https://schema.org'),
    )
    schema_custom_json = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Custom Schema JSON'),
        help_text=_('Optional: paste full JSON-LD here to override auto-generated schema.'),
    )

    def __str__(self):
        return self.title[:50]

    def get_schema_json(self):
        if self.schema_custom_json:
            return self.schema_custom_json

        data = {
            "@context": self.schema_context or "https://schema.org",
            "@type": self.schema_type or "BlogPosting",
            "headline": self.seo_title or self.title,
            "description": self.seo_description,
            "datePublished": self.created_at.isoformat() if self.created_at else None,
        }
        if self.author_name:
            data["author"] = {
                "@type": "Person",
                "name": self.author_name,
            }

        image_url = None
        if self.og_image:
            image_url = self.og_image
        elif self.og_image_file:
            try:
                image_url = self.og_image_file.url
            except ValueError:
                pass
        elif self.image:
            try:
                image_url = self.image.url
            except ValueError:
                pass

        if image_url:
            data["image"] = image_url

        data = {k: v for k, v in data.items() if v is not None}

        return json.dumps(data, ensure_ascii=False)
