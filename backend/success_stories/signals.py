################################################
"""
SUCCESS STORIES SIGNALS HERE.
"""
################################################
from django.db.models.signals import pre_save
from django.dispatch import receiver
from success_stories.models import SuccessStorie
from utils.slug import GENERATE_SLUG

@receiver(pre_save, sender=SuccessStorie)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
        