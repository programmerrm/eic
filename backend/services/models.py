####################################################
"""
SERVICES MODELS HERE.
"""
####################################################
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from utils.validate_image_size import VALIDATE_IMAGE_SIZE
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION

# CREATE MODELS HERE.

# ========== SERVICE PAGE TOP BAR ============
class ServicePageTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your service page top bar title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service page top bar description...'),
    )

    class Meta:
        verbose_name = _('Service Page Top Bar')
        verbose_name_plural = _('Service Page Top Bar')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ServicePageTopBar.objects.exclude(id=self.id).delete()

    def __str__(self):
        return f"Service page top bar title is {self.title[:50]}"

# ========== SERVER CATEGORIES ===============
class Categories(models.Model):
    name = models.CharField(
        max_length=280,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name

# ================ SERVICE ==================
class Service(models.Model):
    image = models.FileField(
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
        help_text=_('Upload your service image...'),
    )
    title = models.CharField(
        unique=True,
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    slug = models.SlugField(
        unique=True,
        max_length=280,
        editable=False,
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )
    categories = models.ManyToManyField(
        Categories,
        related_name="services",
        verbose_name=_("Service Categories")
    )

    def __str__(self):
        return f"Service title : {self.title[:50]}"

# ======== Services Include Top Title ===========
class ServicesIncludeTopTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='include_top_title',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title[:50]

# =========== Services Include Top Item ============
class ServicesIncludeTopItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='include_top_items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    image = models.FileField(
        upload_to='services-include-top/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title[:50]

# =========== Service Item Main =============
class ServiceItemMain(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='main_item',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    normal_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Normal Title'),
        help_text=_('Enter your service main normal title...'),
    )
    span_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Span Title'),
        help_text=_('Enter your service main normal span title...'),
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ServiceItemMain.objects.exclude(id=self.id).delete()

    def __str__(self):
        return f"Service item main infomation added."

# ============== Service Item ================
class ServiceItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    image = models.FileField(
        upload_to='services',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('Image'),
        help_text=_('Upload your service item image...'),
    )
    title = models.CharField(
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )

    def __str__(self):
        return f"Service item title : {self.title[:50]}"




# ============ Service Why Choose Us Title =============
class ServiceWhyChooseUsTitle(models.Model):
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
    image = models.ImageField(
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        ServiceWhyChooseUsTitle.objects.exclude(id=self.id).delete()

    def __str__(self):
        return self.title_span[:50]

# ============ Service Why Choose Us Item =============
class ServiceWhyChooseUsItem(models.Model):
    name = models.CharField(
        unique=True,
        max_length=280,
        verbose_name=_('Name'),
        help_text=_('Enter service item why choose us item name...'),
    )

    def __str__(self):
        return f"Service item why choose us item name : {self.name[:50]}"

# ========= Service Paymnet ===========
class ServicePaymnet(models.Model):
    image = models.ImageField(
        upload_to='services/',
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
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
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title_span[:50]



# ======== Services Include Bottom Title ===========
class ServicesIncludeBottomTitle(models.Model):
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name='include_bottom_title',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title[:50]

# =========== Services Include Bottom Item ============
class ServicesIncludeBottomItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='include_bottom_items',
        verbose_name=_("Service"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title[:50]

# ========== FAQ ==========
class Faq(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='faqs',
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
        help_text=_('Select the service this FAQ belongs to...'),
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('FAQ Title'),
        help_text=_('Enter your FAQ title...')
    )
    image = models.FileField(
        upload_to='faq/',
        validators=[VALIDATE_IMAGE_EXTENSION],
        verbose_name=_('FAQ File')
    )

    def __str__(self):
        return self.title[:50]

# ========== FAQ ITEM ==========
class FaqItem(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='faq_items',
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
        help_text=_('Select the service this FAQ item belongs to...'),
        blank=True,
        null=True,
    )
    question = models.CharField(
        max_length=280,
        verbose_name=_('Question'),
        help_text=_('Enter your FAQ question...')
    )
    answer = models.TextField(
        verbose_name=_('Answer'),
        help_text=_('Enter your FAQ answer...')
    )

    def __str__(self):
        return self.question[:50]
    