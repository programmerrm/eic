####################################################
"""
HOMEPAGE MODELS HERE.
"""
####################################################
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from utils.validate_video_size import VALIDATE_VIDEO_SIZE
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION
from utils.validate_image_size import VALIDATE_IMAGE_SIZE

# CREATE MODELS HERE.

# ================= BANNER ====================
# class Banner(models.Model):
#     video_file = models.FileField(
#         null=True,
#         blank=True,
#         upload_to='videos/',
#         validators=[VALIDATE_VIDEO_SIZE],
#         verbose_name=_('Video'),
#         help_text=_('Upload banner section video file...'),
#     )
#     title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=280,
#         validators=[MinLengthValidator(3)],
#         verbose_name=_('Title'),
#         help_text=_('Enter your banner title...')
#     )
#     sub_title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=280,
#         validators=[MinLengthValidator(3)],
#         verbose_name=_('Sub Title'),
#         help_text=_('Enter your banner sub title...')
#     )
#     description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('Description'),
#         help_text=_('Enter your banner description...'),
#     )
#     short_description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('Short Description'),
#         help_text=_('Enter your banner short description...'),
#     )
#     payment_logo = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='banner/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Paymnet Logo'),
#         help_text=_('Upload your payment logo...'),
#     )
#     get_started_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Get Started Button Name'),
#         help_text=_('Enter get started button name...'),
#     )
#     get_started_url = models.URLField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Get Started Button URL'),
#         help_text=_('Enter get started button URL...'),
#     )

#     secure_business_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Secure My Business Button Name'),
#         help_text=_('Enter secure my business button name...'),
#     )
#     secure_business_url = models.URLField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Secure My Business Button URL'),
#         help_text=_('Enter secure my business button URL...'),
#     )

#     company_profile_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Company Profile Button Name'),
#         help_text=_('Enter company profile button name...'),
#     )
#     company_profile_url = models.URLField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Company Profile Button URL'),
#         help_text=_('Enter company profile button URL...'),
#     )

#     def __str__(self):
#         return f"{self.title}"

# ================= SECURITY ====================
# class SecurityFirm(models.Model):
#     bg = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='security-firm/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Security Firm BG'),
#         help_text=_('Upload your security firm bg image...'),
#     )
#     title_span = models.CharField(
#         max_length=280,
#         null=True,
#         blank=True,
#         verbose_name="Title (span part)",
#         help_text="This part will be wrapped in <span> in frontend",
#     )
#     title_normal = models.CharField(
#         max_length=280,
#         null=True,
#         blank=True,
#         verbose_name="Title (normal part)",
#         help_text="This part will be outside <span> in frontend",
#     )
#     main_img = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='security-firm/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Main Image'),
#         help_text=_('Upload your security firm image...'),
#     )
#     sub_img = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='security-firm/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Main Image'),
#         help_text=_('Upload your security firm image...'),
#     )
#     left_side_animation_img = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='security-firm/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Left side animation image'),
#         help_text=_('Upload your security firm left side animation image...'),
#     )
#     right_side_animation_img = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='security-firm/',
#         validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
#         verbose_name=_('Right side animation image'),
#         help_text=_('Upload your security firm right side animation image...'),
#     )
#     mission_title = models.CharField(
#         max_length=280,
#         null=True,
#         blank=True,
#         verbose_name="Mission Title",
#     )
#     mission_description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('Mission description')
#     )
#     vision_title = models.CharField(
#         max_length=280,
#         null=True,
#         blank=True,
#         verbose_name="Vision Title",
#     )
#     vision_description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('Vision description')
#     )
#     get_to_know_us_btn_name = models.CharField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Get To Know Us Button Name'),
#         help_text=_('Enter get to know us button name...'),
#     )
#     get_to_know_us_btn_url = models.URLField(
#         null=True,
#         blank=True,
#         max_length=180,
#         verbose_name=_('Get To Know Us Button URL'),
#         help_text=_('Enter get to know us button URL...'),
#     )
#     security_persentences = models.IntegerField(
#         verbose_name=_('Security Persentences'),
#         default=0,
#     )
#     ability_persentences = models.IntegerField(
#         verbose_name=_('Security Persentences'),
#         default=0,
#     )
#     solving_persentences = models.IntegerField(
#         verbose_name=_('Security Persentences'),
#         default=0,
#     )

#     def __str__(self):
#         return super().__str__()

# class CybersecuritySolutionTitle(models.Model):
#     title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=280,
#         verbose_name=_('Cyber Security Solution Title'),
#     )
#     description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('Cyber Security Solution Description')
#     )
#     image = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='cyber-ecurity/',
#         verbose_name=_('Cyber Security Solution Image'),
#     )

#     def __str__(self):
#         return f"Cyber Security Solution Title"

# class CybersecuritySolutionItem(models.Model):
#     image = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='cybers-ecurity/',
#         verbose_name=_('Cyber Security Solution Item Image'),
#         help_text=_('Upload cyber security solution item image...'),
#     )
#     title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=280,
#         verbose_name=_('Cyber Security Solution Item Title'),
#         help_text=_('Enter cyber security solution item title...'),
#     )
#     count = models.IntegerField(
#         default=0,
#         verbose_name=_('Cyber Security Solution Item Count'),
#         help_text=_('Enter cyber security solution item count...'),
#     )

#     def __str__(self):
#         return f"Cyber Security Solution Item"
    
# class OurProvenProcessSecurity(models.Model):
#     image = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='our-proven-process-security/',
#         verbose_name=_('our proven process security image'),
#     )
#     title_before_span = models.CharField(
#         max_length=280, 
#         blank=True, 
#         null=True,
#         verbose_name=_('our proven process security title before span'),
#         help_text=_('Enter your our proven process security before span...'),
#     )
#     title_span = models.CharField(
#         max_length=280, 
#         blank=True, 
#         null=True,
#         verbose_name=_('our proven process security title span'),
#         help_text=_('Enter your our proven process security title span...'),
#     )
#     title_after_span = models.CharField(
#         max_length=280, 
#         blank=True, 
#         null=True,
#         verbose_name=_('our proven process security title after span'),
#         help_text=_('Enter your our proven process security title after span...'),
#     )
#     description = models.TextField(
#         blank=True, 
#         null=True,
#         verbose_name=_('our proven process security description'),
#     )
    
#     def __str__(self):
#         return f"our proven process security"

# class OurProvenProcessSecurityItems(models.Model):
#     image = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='our-proven-process-security/',
#         verbose_name=_('our proven process security item image'),
#     )
#     title = models.CharField(
#         null=True,
#         blank=True,
#         max_length=280,
#         verbose_name=_('our proven process security item title'),
#     )
#     description = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_('our proven process security item description'),
#     )

#     def __str__(self):
#         return f"Our proven process security item {self.title}"
    