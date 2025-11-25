################################################
"""
BLOGS SIGNALS HERE.
"""
################################################
from django.db.models.signals import pre_save
from django.dispatch import receiver
from blogs.models import Blog
from utils.slug import GENERATE_SLUG

@receiver(pre_save, sender=Blog)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
        