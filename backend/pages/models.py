import json
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=280, unique=True)
    slug = models.SlugField(max_length=280, unique=True)

    def __str__(self):
        return self.name
    
class SeoTag(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="seo"
    )

    # Basic SEO
    title = models.CharField(null=True, blank=True, max_length=380)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=280)

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

class Schema(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="schema"
    )
    name = models.CharField(max_length=255)
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
            "@id": f"{self.url}#page",
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
    name = models.CharField(max_length=255)
    url = models.URLField()
    logo = models.URLField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    page_schema = models.OneToOneField(
        Schema,
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
