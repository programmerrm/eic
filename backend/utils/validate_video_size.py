#################################################
"""
VALIDATE VIDEO SIZE HERE.
"""
#################################################
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# ======== VALIDATE VIDEO SIZE ========
def VALIDATE_VIDEO_SIZE(video):
    max_size = 50 * 1024 * 1024
    if video.size > max_size:
        raise ValidationError(_('The video file size must be less than 50 MB.'))
    