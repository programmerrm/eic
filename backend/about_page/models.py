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
        default="AboutPage",
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
    