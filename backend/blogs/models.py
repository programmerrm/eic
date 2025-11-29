####################################################
"""
BLOGS MODELS HERE.
"""
####################################################
import json
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from ckeditor_uploader.fields import RichTextUploadingField

# ==================== BLOG PAGE SEO TAGS ====================
class SeoTag(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('SEO Title'),
        help_text=_('The title of the page for search engines and browser tab.')
    )
    description = models.TextField(
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

    def __str__(self):
        return self.title

# ==================== BLOG PAGE SCHEMA ====================
class Schema(models.Model):
    context = models.CharField(
        max_length=255,
        default="https://schema.org",
        verbose_name=_('Context'),
        help_text=_('Always https://schema.org')
    )
    type = models.CharField(
        max_length=50,
        default="ContactPage",
        verbose_name=_('Type'),
        help_text=_('@type for JSON-LD')
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Page Name'),
        help_text=_('The name/title of the page.')
    )
    url = models.URLField(
        verbose_name=_('URL'),
        help_text=_('Full URL of the page.')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Page description for schema.org.')
    )
    contact_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_('Contact Type'),
        help_text=_('contactType for schema.org, e.g., Customer Support.')
    )
    email = models.EmailField(
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

# ============== BLOG TOP BAR ====================
class BlogTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your blog section top bar title...')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=('Enter your blog section top bar description...')
    )

    class Meta:
        verbose_name = 'Blog Top Bar'
        verbose_name_plural = _('Blog Top Bar')

    def __str__(self):
        return f"Blog top bar data infomation added."

# ================= TAG =========================
class Tag(models.Model):
    name = models.CharField(
        max_length=255, 
        unique=True,
        verbose_name=_('Tag Name'),
        help_text=_('Enter tag name...'),
    )

    def __str__(self):
        return self.name

# ================= BLOG =========================
class Blog(models.Model):
    image = models.FileField(
        upload_to='blogs',
        validators=[VALIDATE_IMAGE_EXTENSION],
        null=True,
        blank=True,
        verbose_name=_('Image'),
        help_text=_('Upload your blog image...'),
    )
    title = models.CharField(
        max_length=500,
        unique=True,
        verbose_name=_('Title'),
        help_text=_('Enter your blog title...'),
    )
    slug = models.SlugField(
        editable=False,
        unique=True,
        verbose_name=_('Slug'),
    )
    content = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_('Content'),
        help_text=_('Enter your blog content...'),
    )
    author_image = models.FileField(
        null=True,
        blank=True,
        upload_to='blogs/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Author Image'),
        help_text=_('Upload blog author image...'),
    )
    author_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    author_bio = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    author_description = models.TextField(
        null=True,
        blank=True,
    )

    author_facebook_url = models.URLField(blank=True, null=True)
    author_twitter_url = models.URLField(blank=True, null=True)
    author_medium_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, related_name="blogs", blank=True)

    def __str__(self):
        return self.title
