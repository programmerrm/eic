####################################################
"""
TERMS & CONDITIONS MODELS HERE.
"""
####################################################
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# CREATE MODELS HERE.

# =============== TERMS & CONDITIONSTOP BAR =================
class TermsConditionTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter terms & condition title...'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Enter terms & condition  description...'),
    )

    class Meta:
        verbose_name = _('Terms Condition Top Bar')
        verbose_name_plural = _('Terms Condition Top Bar')

    def __str__(self):
        return f"Terms & condition title is : {self.title[:50]}"

# ============== TERMS & CONDITION CONTENT =================
class TermsConditionContent(models.Model):
    content = RichTextUploadingField(
        verbose_name=_('Content'),
        help_text=_('Enter the terms & condition content here...'),
    )

    class Meta:
        verbose_name = _('Terms Condition Content')
        verbose_name_plural = _('Terms Condition Content')

    def __str__(self):
        return f"Terms & condition content uploaded."
