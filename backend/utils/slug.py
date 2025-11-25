######################################################
"""
GENERATE SLUG HERE.
"""
######################################################
from django.utils.text import slugify

# ========== GENERATE SLUG =============
def GENERATE_SLUG(value):
    try:
        return slugify(value)
    except Exception as e:
        raise ValueError(f"Slug generation failed: {e}")
    