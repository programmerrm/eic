################################################
"""
SUCCESS STORIES SIGNALS HERE.
"""
################################################
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from success_stories.models import SuccessStorie, SeoTag, Schema, SuccessStorieTopBar
from django.core.cache import cache
from utils.slug import GENERATE_SLUG
from success_stories.cache import SUCCESS_STORIES_SEO_TAG_CACHE_KEY, SUCCESS_STORIES_SCHEMA_CACHE_KEY, SUCCESS_STORIES_TOP_BAR_CACHE_KEY, ALL_SUCCESS_STORIES_CACHE_KEY

@receiver([post_save, post_delete], sender=SeoTag)
def clear_seo_tag_cache(sender, **kwargs):
    cache.delete(SUCCESS_STORIES_SEO_TAG_CACHE_KEY)

@receiver([post_save, post_delete], sender=Schema)
def clear_schema_cache(sender, **kwargs):
    cache.delete(SUCCESS_STORIES_SCHEMA_CACHE_KEY)

@receiver([post_save, post_delete], sender=SuccessStorieTopBar)
def clear_success_storie_top_bar_cache(sender, **kwargs):
    cache.delete(SUCCESS_STORIES_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=SuccessStorie)
def clear_all_success_storie_cache(sender, **kwargs):
    cache.delete(ALL_SUCCESS_STORIES_CACHE_KEY)

@receiver(pre_save, sender=SuccessStorie)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
        