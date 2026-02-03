####################################################
"""
ABOUT PAGE MODELS HERE.
"""
####################################################
from django.db import models
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from django.utils.translation import gettext_lazy as _

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
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Title'),
    )
    image = models.FileField(
        upload_to='secure-future/',
        null=True,
        blank=True,
        verbose_name=_('Image'),
    )
    alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Alt')
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
        max_length=280,
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
        max_length=280,
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

class SecurityFirm(models.Model):
    bg = models.FileField(
        null=True,
        blank=True,
        upload_to='security-firm/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Security Firm BG'),
        help_text=_('Upload your security firm bg image...'),
    )
    bg_image_alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('BG Image Alt'),
    )
    main_img = models.FileField(
        null=True,
        blank=True,
        upload_to='security-firm/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Main Image'),
        help_text=_('Upload your security firm image...'),
    )
    main_image_alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Main Image Alt'),
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
    