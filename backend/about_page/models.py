from django.db import models
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# ========= ABOUT TOP BAR =================
class AboutTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your about section top bar title...')
    )
    description = models.TextField(
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

    def __str__(self):
        return self.title or "Secure Future Item"

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

    def __str__(self):
        return self.title or "Digital security solution top bar"

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

    def __str__(self):
        return self.title or "Digital Security Solution Item"
    
class HappyJourneyTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )

    def __str__(self):
        return self.title or "Happy Journey Top Bar"

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

    def __str__(self):
        return self.title or "Happy Journey Item"

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
    
    def __str__(self):
        return self.title_span or "Security Firm"
    