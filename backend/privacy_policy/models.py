####################################################
"""
PRIVACY_POLICY MODELS HERE.
"""
####################################################
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# CREATE MODELS HERE.

# =============== PRIVACY POLICY TOP BAR =================
class PrivacyPolicyTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter privacy policy title...'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Enter privacy policy description...'),
    )

    class Meta:
        verbose_name = _('Privacy Policy Top Bar')
        verbose_name_plural = _('Privacy Policy Top Bar')

    def __str__(self):
        return f"Privacy Policy title is : {self.title[:50]}"

# ============== PRIVACY POLICY CONTENT =================
class PrivacyPolicyContent(models.Model):
    content = RichTextUploadingField(
        verbose_name=_('Content'),
        help_text=_('Enter the privacy policy content here...'),
    )

    class Meta:
        verbose_name = _('Privacy Policy Content')
        verbose_name_plural = _('Privacy Policy Content')

    def __str__(self):
        return f"Privacy Policy content uploaded."
