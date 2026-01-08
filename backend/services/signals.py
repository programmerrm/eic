from django.db.models.signals import pre_save, post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from services.models import Service, SeoTag, Schema, ServicePageTopBar
from utils.trigger_nextjs_revalidate import trigger_nextjs_revalidate
from utils.slug import GENERATE_SLUG
from services.cache import SERVICE_SEO_TAGS_CACHE_KEY, SERVICE_SCHEMA_CACHE_KEY, SERVICE_PAGE_TOP_BAR_CACHE_KEY, ALL_SERVICES_CACHE_KEY

@receiver([post_save, post_delete], sender=SeoTag)
def clear_seo_tag_cache(sender, **kwargs):
    cache.delete(SERVICE_SEO_TAGS_CACHE_KEY)

@receiver([post_save, post_delete], sender=Schema)
def clear_schema_cache(sender, **kwargs):
    cache.delete(SERVICE_SCHEMA_CACHE_KEY)

@receiver([post_save, post_delete], sender=ServicePageTopBar)
def clear_service_page_top_bar_cache(sender, **kwargs):
    cache.delete(SERVICE_PAGE_TOP_BAR_CACHE_KEY)
    trigger_nextjs_revalidate("/services/top-bar/");

@receiver([post_save, post_delete], sender=Service)
def clear_service_cache(sender, **kwargs):
    cache.delete(ALL_SERVICES_CACHE_KEY)
    trigger_nextjs_revalidate("/services/list-items/");

@receiver(pre_save, sender=Service)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = GENERATE_SLUG(instance.title)
        