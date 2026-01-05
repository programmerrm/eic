################################################
"""
BLOGS SIGNALS HERE.
"""
################################################
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from blogs.models import Blog, SeoTag, Schema, BlogTopBar
from utils.slug import GENERATE_SLUG
from django.core.cache import cache
from blogs.cache import BLOG_SEO_TAG_CACHE_KEY, BLOG_SCHEMA_CACHE_KEY, BLOG_TOP_BAR_CACHE_KEY, ALL_BLOGS_CACHE_KEY

@receiver([post_save, post_delete], sender=SeoTag)
def clear_seo_tag_cache(sender, **kwargs):
    cache.delete(BLOG_SEO_TAG_CACHE_KEY)

@receiver([post_save, post_delete], sender=Schema)
def clear_schema_cache(sender, **kwargs):
    cache.delete(BLOG_SCHEMA_CACHE_KEY)

@receiver([post_save, post_delete], sender=BlogTopBar)
def clear_blog_top_bar_cache(sender, **kwargs):
    cache.delete(BLOG_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=Blog)
def clear_all_blog_cache(sender, **kwargs):
    cache.delete(ALL_BLOGS_CACHE_KEY)

@receiver(pre_save, sender=Blog)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
        