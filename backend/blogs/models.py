####################################################
"""
BLOGS MODELS HERE.
"""
####################################################
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from ckeditor_uploader.fields import RichTextUploadingField

# ============== BLOG TOP BAR ====================
class BlogTopBar(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your blog section top bar title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=('Enter your blog section top bar description...')
    )

    class Meta:
        verbose_name = 'Blog Top Bar'
        verbose_name_plural = _('Blog Top Bar')

    def __str__(self):
        return f"Blog top bar data infomation added."

# ================= TAG =========================
class Tag(models.Model):
    name = models.CharField(
        max_length=255, 
        unique=True,
        verbose_name=_('Tag Name'),
        help_text=_('Enter tag name...'),
    )

    def __str__(self):
        return self.name

# ================= BLOG =========================
class Blog(models.Model):
    image = models.FileField(
        upload_to='blogs',
        null=True,
        blank=True,
        verbose_name=_('Image'),
        help_text=_('Upload your blog image...'),
    )
    blog_image_alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Blog Image Alt'),
    )
    title = models.CharField(
        max_length=500,
        unique=True,
        verbose_name=_('Title'),
        help_text=_('Enter your blog title...'),
    )
    slug = models.SlugField(
        editable=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    content = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_('Content'),
        help_text=_('Enter your blog content...'),
    )
    author_image = models.FileField(
        null=True,
        blank=True,
        upload_to='blogs/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Author Image'),
        help_text=_('Upload blog author image...'),
    )
    author_image_alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Author Image Alt'),
    )
    author_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    author_bio = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    author_description = models.TextField(
        null=True,
        blank=True,
    )

    author_facebook_url = models.URLField(blank=True, null=True)
    author_twitter_url = models.URLField(blank=True, null=True)
    author_medium_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(
        Tag,
        related_name="blogs",
        blank=True,
        verbose_name=_('Tag'),
    )

    def __str__(self):
        return "Blog added"
    