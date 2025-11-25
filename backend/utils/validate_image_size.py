#################################################
"""
VALIDATE IMAGE SIZE HERE.
"""
#################################################
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# ======== VALIDATE IMAGE SIZE ========
def VALIDATE_IMAGE_SIZE(image):
    max_size = 10 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(_('The image file size must be less than 10 MB.'))
    