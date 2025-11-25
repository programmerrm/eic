from django.db.models.signals import pre_save
from django.dispatch import receiver
from pages.models import Pages
from utils.slug import GENERATE_SLUG

@receiver(pre_save, sender=Pages)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.name)
        