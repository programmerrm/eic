####################################################
"""
ABOUT PAGE MODELS HERE.
"""
####################################################
import json
from django.db import models
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from django.utils.translation import gettext_lazy as _

# ============= SEO TAGS =================
class SeoTag(models.Model):
    # Basic SEO
    title = models.CharField(null=True, blank=True, max_length=380)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=280, null=True, blank=True,)

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

class AboutPageSchema(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True,)
    url = models.URLField(null=True, blank=True,)
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
    name = models.CharField(max_length=255, null=True, blank=True,)
    url = models.URLField(null=True, blank=True,)
    logo = models.URLField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    homepage_schema = models.OneToOneField(
        AboutPageSchema,
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

# ========= ABOUT TOP BAR =================
class AboutTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your about section top bar title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=('Enter your about section top bar description...')
    )

    class Meta:
        verbose_name = 'About Top Bar'
        verbose_name_plural = _('About Top Bar')

    def __str__(self):
        return f"About top bar data infomation added."
    
class SecureFutureTopBar(models.Model):
    normal_title = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Normal Title'),
    )
    title_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Title span'),
    )

    class Meta:
        verbose_name = 'Secure Future Top Bar'
        verbose_name_plural = _('Secure Future Top Bar')

    def __str__(self):
        return self.normal_title or "Secure Future Top Bar"

class SecureFutureItem(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )
    image = models.FileField(
        upload_to='secure-future/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        null=True,
        blank=True,
        verbose_name=_('Image'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = 'Secure Future Items'
        verbose_name_plural = _('Secure Future Items')

    def __str__(self):
        return self.title[:50] or "Secure Future Item"

class DigitalSecuritySolutionTopBar(models.Model):
    title = models.CharField(
        max_length=380,
        verbose_name=_('Title'),
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = 'Digital Security Solution Top Bar'
        verbose_name_plural = _('Digital Security Solution Top Bar')

    def __str__(self):
        return self.title[:50] or "Digital security solution top bar"

class DigitalSecuritySolutionItem(models.Model):
    count = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('Count'),
    )
    title = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = 'Digital Security Solution Items'
        verbose_name_plural = _('Digital Security Solution Items')

    def __str__(self):
        return self.title or "Digital Security Solution Item"
    
class HappyJourneyTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )

    class Meta:
        verbose_name = 'Happy Journey Top Bar'
        verbose_name_plural = _('Happy Journey Top Bar')

    def __str__(self):
        return self.title[:50] or "Happy Journey Top Bar"

class HappyJourneyItem(models.Model):
    year = models.IntegerField(
        verbose_name=_('Year'),
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=380,
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = 'Happy Journey Items'
        verbose_name_plural = _('Happy Journey Items')

    def __str__(self):
        return self.title[:50] or "Happy Journey Item"

# ================= SECURITY ====================
class SecurityFirm(models.Model):
    bg = models.FileField(
        null=True,
        blank=True,
        upload_to='security-firm/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Security Firm BG'),
        help_text=_('Upload your security firm bg image...'),
    )
    main_img = models.FileField(
        null=True,
        blank=True,
        upload_to='security-firm/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Main Image'),
        help_text=_('Upload your security firm image...'),
    )
    title_span = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name="Title (span part)",
        help_text="This part will be wrapped in <span> in frontend",
    )
    title_normal = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name="Title (normal part)",
        help_text="This part will be outside <span> in frontend",
    )
    mission_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name="Mission Title",
    )
    mission_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Mission description'),
    )
    vision_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name="Vision Title",
    )
    vision_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Vision description'),
    )
    get_to_know_us_btn_name = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Get To Know Us Button Name'),
        help_text=_('Enter get to know us button name...'),
    )
    get_to_know_us_btn_url = models.URLField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Get To Know Us Button URL'),
        help_text=_('Enter get to know us button URL...'),
    )

    class Meta:
        verbose_name = 'Security Firm'
        verbose_name_plural = _('Security Firm')
    
    def __str__(self):
        return self.title_span[:50] or "Security Firm"
    