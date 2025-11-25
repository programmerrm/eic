######################################################
"""
VALIDATE IMAGE EXTENSION HERE.
"""
######################################################
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# ========== VALIDATE IMAGE EXTENSION =============
def VALIDATE_IMAGE_EXTENSION(image):
    ext = os.path.splitext(image.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg']
    if ext not in valid_extensions:
        raise ValidationError(
            _(f'Unsupported file extension "{ext}". Allowed types: JPG, JPEG, PNG, WEBP, SVG.')
        )
    