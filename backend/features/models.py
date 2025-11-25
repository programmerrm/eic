from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from utils.validate_image_size import VALIDATE_IMAGE_SIZE

# Create your models here.

# ============== Feature ================
class Feature(models.Model):
    title_before_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Feature title before span'),
        help_text=_('Upload your feature title before span...'),
    )
    title_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Feature title span'),
        help_text=_('Upload your feature title span...'),
    )
    title_after_span = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name=_('Feature title after span'),
        help_text=_('Upload your feature title after span...'),
    )
    features_btn_name = models.CharField(
        max_length=180,
        null=True,
        blank=True,
        verbose_name=_('Features Button Name'),
    ) 
    features_btn_url = models.URLField(
        max_length=180,
        null=True,
        blank=True,
        verbose_name=_('Features Button URL'),
    )

    class Meta:
        verbose_name = _('Feature Top Bar')
        verbose_name_plural = _('Feature Top Bar')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        Feature.objects.exclude(id=self.id).delete()

    def __str__(self):
        return f"Feature item added"

# ================= Feature Item =================
class FeatureItem(models.Model):
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='features/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Feature Image'),
        help_text=_('Upload your feature image...'),
    )

    bg = models.FileField(
        null=True,
        blank=True,
        upload_to='features/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Feature BG Image'),
        help_text=_('Upload your feature bg image...'),
    )

    name = models.CharField(
        max_length=280,
        unique=True,
        verbose_name=_('Feature Name'),
        help_text=_('Enter your feature name...'),
    )
    slug = models.SlugField(
        max_length=280,
        unique=True,
        editable=False,
        verbose_name=_('Feature Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Feature Description'),
        help_text=_('Enter your feature description...'),
    )

    class Meta:
        verbose_name = _('Feature-Item')
        verbose_name_plural = _('Feature-Item')

    def __str__(self):
        return f"Feature name is {self.name}"
