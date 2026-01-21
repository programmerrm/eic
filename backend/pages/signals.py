from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from pages.models import Page
from pages.cache import PAGE_LIST_CACHE_KEY, SINGLE_PAGE_CACHE_KEY

@receiver([post_save, post_delete], sender=Page)
def clear_page_cache(sender, instance, **kwargs):
    cache.delete(PAGE_LIST_CACHE_KEY)
    cache.delete(f"{SINGLE_PAGE_CACHE_KEY}:{instance.slug}")

