from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from features.models import Feature, FeatureItem
from utils.slug import GENERATE_SLUG
from features.cache import FEATURE_CACHE_KEY, FEATURE_ITEM_CACHE_KEY

@receiver(pre_save, sender=FeatureItem)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.name)

@receiver([post_save, post_delete], sender=Feature)
def clear_feature_cache(sender, **kwargs):
    cache.delete(FEATURE_CACHE_KEY)

@receiver([post_save, post_delete], sender=FeatureItem)
def clear_feature_item_cache(sender, **kwargs):
    cache.delete(FEATURE_ITEM_CACHE_KEY)
        