####################################################
"""
FAQ MODELS HERE.
"""
####################################################
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from utils.validate_image_size import VALIDATE_IMAGE_SIZE

# CREATE MODELS HERE.

# ================== FAQ TOP BAR =================
class FaqTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your faq top bar title...'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Enter your faq top bar description...'),
    )

    def __str__(self):
        return f"Faq top bar title : {self.title[:50]}"
    
# =============== FAQ SECTION ======================
class FaqSection(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your faq section title...'),
    )
    image = models.ImageField(
        upload_to='faq/',
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
        help_text=_('Upload your faq section image...'),
    )

    def __str__(self):
        return f"Faq section title : {self.title[:50]}"

# =============== FAQ ITEMS =======================
class FaqItem(models.Model):
    question = models.CharField(
        max_length=280,
        verbose_name=_('Question'),
        help_text=_('Enter your faq item question...'),
    )
    answer = RichTextUploadingField(
        verbose_name=_('Answer'),
        help_text=_('Enter your faq item answer...'),
    )

    def __str__(self):
        return f"Faq item question : {self.question[:50]}"
