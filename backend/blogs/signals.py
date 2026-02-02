from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.cache import cache
from blogs.models import Blog, BlogTopBar
from blogs.cache import (
    BLOG_TOP_BAR_CACHE_KEY,
    ALL_BLOGS_CACHE_KEY,
    SINGLE_BLOG_CACHE_KEY
)
from utils.slug import GENERATE_SLUG

@receiver([post_save, post_delete], sender=BlogTopBar)
def clear_blog_top_bar_cache(sender, **kwargs):
    cache.delete(BLOG_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=Blog)
def clear_blog_cache(sender, instance, **kwargs):
    cache.delete_pattern(f"{ALL_BLOGS_CACHE_KEY}*")

    if instance.slug:
        cache.delete(f"{SINGLE_BLOG_CACHE_KEY}_{instance.slug}")

@receiver(pre_save, sender=Blog)
def set_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
