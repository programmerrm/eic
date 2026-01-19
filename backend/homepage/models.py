####################################################
"""
HOMEPAGE MODELS HERE.
"""
####################################################
import json
from django.db import models
from django.core.validators import MinLengthValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from django.core.validators import MinValueValidator, MaxValueValidator

# CREATE MODELS HERE.

# ==================== HOME PAGE SEO TAGS ====================
class SeoTag(models.Model):
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

class HomePageSchema(models.Model):
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
    name = models.CharField(max_length=255)
    url = models.URLField()
    logo = models.URLField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    homepage_schema = models.OneToOneField(
        HomePageSchema,
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

# ================= BANNER ====================
class Banner(models.Model):
    image = models.FileField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_EXTENSION],
        upload_to='banner/',
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Title'),
        help_text=_('Enter your banner title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your banner description...'),
    )
    secure_business_btn_name = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Secure My Business Button Name'),
        help_text=_('Enter secure my business button name...'),
    )
    secure_business_btn_url = models.URLField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Secure My Business Button URL'),
        help_text=_('Enter secure my business button URL...'),
    )
    company_profile_btn_name = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Company Profile Button Name'),
        help_text=_('Enter company profile button name...'),
    )
    company_profile_btn_url = models.URLField(
        null=True,
        blank=True,
        max_length=180,
        verbose_name=_('Company Profile Button URL'),
        help_text=_('Enter company profile button URL...'),
    )

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = _('Banner')

    def __str__(self):
        return f"{self.title[:50]}" or "Banner"

# ================ Paymnet Info ===================
class PaymnetInfo(models.Model):
    image = models.FileField(
        upload_to='paymnets/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        null=True,
        blank=True,
        verbose_name=_('Image'),
        help_text=_('Payment logo'),
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
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )
    btn_name = models.CharField(
        max_length=280,
        verbose_name=_('Button Name'),
        null=True,
        blank=True,
    )
    btn_url = models.URLField(
        verbose_name=_('URL'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = _('Payment')

    def __str__(self):
        return self.title_span[:50] or "Paymnet"

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
    sub_img = models.FileField(
        null=True,
        blank=True,
        upload_to='security-firm/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Sub Image'),
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
    security_persentences = models.IntegerField(
        verbose_name=_('Security Persentences'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    response_persentences = models.IntegerField(
        verbose_name=_('Response Persentences'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    compliance_persentences = models.IntegerField(
        verbose_name=_('Compliance Persentences'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    def __str__(self):
        return self.title_span or "Security Firm"

# =============== Cyber Security Solution Title ================
class CybersecuritySolutionTitle(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Cyber Security Title'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Cyber Security Description')
    )
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='cyber-ecurity/',
        verbose_name=_('Cyber Security Image'),
    )

    class Meta:
        verbose_name = 'Cybersecurity Excellence Title'
        verbose_name_plural = _('Cybersecurity Excellence Title')

    def __str__(self):
        return f"Cyber Security Solution Title"

# =========== Cyber Security Solution Item =============
class CybersecuritySolutionItem(models.Model):
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='cybers-ecurity/',
        verbose_name=_('Cyber Security Item Image'),
        help_text=_('Upload cyber security item image...'),
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Cyber Security Item Title'),
        help_text=_('Enter cyber security item title...'),
    )
    count = models.IntegerField(
        default=0,
        verbose_name=_('Cyber Security Item Count'),
        help_text=_('Enter cyber security item count...'),
    )

    class Meta:
        verbose_name = 'Cybersecurity Excellence Items'
        verbose_name_plural = _('Cybersecurity Excellence Items')

    def __str__(self):
        return f"Cyber Security Solution Item"
    
# ========= Our Proven Process Security ===========
class OurProvenProcessSecurity(models.Model):
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='our-proven-process-security/',
        verbose_name=_('our proven process security image'),
    )
    title_before_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('our proven process security title before span'),
        help_text=_('Enter your our proven process security before span...'),
    )
    title_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('our proven process security title span'),
        help_text=_('Enter your our proven process security title span...'),
    )
    title_after_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('our proven process security title after span'),
        help_text=_('Enter your our proven process security title after span...'),
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name=_('our proven process security description'),
    )

    class Meta:
        verbose_name = 'Proven Process Security'
        verbose_name_plural = _('Proven Process Security')
    
    def __str__(self):
        return f"our proven process security"

# ========== Our Proven Process Security Items ===========
class OurProvenProcessSecurityItems(models.Model):
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='our-proven-process-security/',
        verbose_name=_('our proven process security item image'),
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('our proven process security item title'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('our proven process security item description'),
    )

    class Meta:
        verbose_name = 'Proven Process Security Items'
        verbose_name_plural = _('Proven Process Security Items')

    def __str__(self):
        return f"Our proven process security item {self.title}"

# =========== REVIEW TOP BAR ===============
class ReviewTopBar(models.Model):
    title_before_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('Review top bar title before span'),
        help_text=_('Enter your review top bar before span...'),
    )
    title_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('Review top bar title span'),
        help_text=_('Enter your review top bar title span...'),
    )
    title_after_span = models.CharField(
        max_length=280, 
        blank=True, 
        null=True,
        verbose_name=_('Review top bar title after span'),
        help_text=_('Enter your review top bar title after span...'),
    )

    class Meta:
        verbose_name = 'Review Top Bar'
        verbose_name_plural = _('Review Top Bar')

    def __str__(self):
        return self.title_span or "Review Top"

# =========== REVIEW ===============
class Review(models.Model):
    author_image = models.FileField(
        validators=[VALIDATE_IMAGE_EXTENSION],
        upload_to='reviews',
        null=True,
        blank=True,
        verbose_name=_('Author Image'),
        help_text=_('Upload review author image...'),
    )
    author_name = models.CharField(
        max_length=180,
        null=True,
        blank=True,
        verbose_name=_('Author Name'),
        help_text=_('Enter review author name...'),
    )
    author_bio = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Author Bio'),
        help_text=_('Enter review author bio...'),
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Review Content'),
        help_text=_('Enter review content...'),
    )

    class Meta:
        verbose_name = 'Reviews'
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return self.author_name or "Autor data"

# ============= Globally Accredited ==============
class GloballyAccredited(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    image = models.FileField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
    )
    bg = models.FileField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Background Image'),
    )

    class Meta:
        verbose_name = 'Globally Accredited'
        verbose_name_plural = _('Globally Accredited')

    def __str__(self):
        return self.title or "Globally Accredited"

# =========== Experience Eic =============
class ExperienceEic(models.Model):
    normal_title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Experience Eic item normal title'),
    )
    span_title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('ExperienceEic item span title'),
    )
    image = models.FileField(
        null=True,
        blank=True,
        verbose_name=_('Image'),
        upload_to='experience-eic/',
    )
    btn_name = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('Button Name'),
    )
    btn_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('Button URL'),
    )

    class Meta:
        verbose_name = 'Experience Top Bar'
        verbose_name_plural = _('Experience Top Bar')

    def __str__(self):
        return self.normal_title or "Experience Eic"

# ========== Experience EicItem =============
class ExperienceEicItem(models.Model):
    name = models.CharField(
        max_length=280,
        verbose_name=_('Item Name'),
    )

    class Meta:
        verbose_name = 'Experience Impact Items'
        verbose_name_plural = _('Experience Impact Items')

    def __str__(self):
        return self.name or "Experience Eic Item"
    