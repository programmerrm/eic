####################################################
"""
CONFIGURATION MODELS HERE.
"""
####################################################
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from utils.validate_image_size import VALIDATE_IMAGE_SIZE
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION

# CREATE MODELS HERE.

# ================ FAVICON MODEL ==============
class Favicon(models.Model):
    icon = models.ImageField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_SIZE],
        upload_to=_('favicon/'),
        verbose_name=_('Favicon'),
        help_text=_('Upload your website favicon...'),
    )

    class Meta:
        verbose_name = _('Favicon')
        verbose_name_plural = _('Favicon')

    def __str__(self):
        return f"Favicon"

# =============== LOGO MODEL ==================
class Logo(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_SIZE],
        upload_to=_('logo/'),
        verbose_name=_('Logo'),
        help_text=_('Upload your website logo...'),
    )
    alt_text = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Logo ALT Text'),
        help_text=_('Enter your logo alt text...'),
    )

    class Meta:
        verbose_name = _('Logo')
        verbose_name_plural = _('Logo')
        
    def __str__(self):
        return f"Logo"

# ============== COPY RIGHT ==================
class CopyRight(models.Model):
    text = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Copy Right Text'),
        help_text=_('Enter your website copy right text...'),
    )

    class Meta:
        verbose_name = _('Copy-Right')
        verbose_name_plural = _('Copy-Right')

    def __str__(self):
        return f"{self.text}"

# ============= SOCIAL LINK ==================
class SocialLink(models.Model):
    icon = models.FileField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Socail Icon'),
        help_text=_('Enter your website socail icon name...')
    )
    url = models.URLField(
        null=True,
        blank=True,
        max_length=280,
        unique=True,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Socail Link URL'),
        help_text=_('Enter your website socail link url...')
    )

    class Meta:
        verbose_name = _('Social-Link')
        verbose_name_plural = _('Social-Link')

    def __str__(self):
        return f"Socail link added"

# ============= NOT FOUND CONTENT ==================
class NotFoundContent(models.Model):
    image = models.FileField(
        upload_to='not-found/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
        help_text=_('Upload your website not found image...'),
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your website not found title...'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Enter your website not found description...')
    )

    def __str__(self):
        return f"Not found infomation added."

# =============== Stay Compliant ===================
class StayCompliant(models.Model):
    image = models.FileField(
        upload_to='stay-compliant/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name='Image',
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    class Meta:
        verbose_name = _('Stay-Compliant')
        verbose_name_plural = _('Stay-Compliant')

    def __str__(self):
        return self.title[:50]

# ============== Compliance Title =================
class ComplianceTitle(models.Model):
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
        verbose_name = _('Compliance-Title')
        verbose_name_plural = _('Compliance-Title')

    def __str__(self):
        return self.title_span[:50]

# ========== Compliance Item List ===========
class ComplianceItemList(models.Model):
    name = models.CharField(
        max_length=280,
        verbose_name=_('Name'),
    )

    class Meta:
        verbose_name = _('Compliance-Item-List')
        verbose_name_plural = _('Compliance-Item-List')
    
    def __str__(self):
        return self.name

# =========== Compliance Item ==============
class ComplianceItem(models.Model):
    image = models.FileField(
        upload_to='compliance/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )

    item_list = models.ManyToManyField(
        ComplianceItemList,
        related_name='items',
    )

    class Meta:
        verbose_name = _('Compliance-Item')
        verbose_name_plural = _('Compliance-Item')

    def __str__(self):
        return self.title[:50]

# =========== Subscribe =============
class Subscribe(models.Model):
    email = models.EmailField(
        max_length=280,
        verbose_name=_('Email'),
        help_text=_('Email Address'),
    )
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ScheduleACall(models.Model):
    number = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name=_('Number'),
    )

    def __str__(self):
        return f"Schedule A Call"
