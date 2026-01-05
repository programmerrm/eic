from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from contact.models import SeoTag, Schema, ContactTopBar,ConatctInfomation, GoogleMap
from contact.cache import CONTACT_SEO_CACHE_KEY, CONTACT_SCHEMA_CACHE_KEY, CONTACT_TOP_BAR_CACHE_KEY, CONTACT_INFOMATION_CACHE_KEY, CONTACT_GOOGLE_MAP_CACHE_KEY

@receiver([post_save, post_delete], sender=SeoTag)
def clear_seo_tag_cache(sender, **kwargs):
    cache.delete(CONTACT_SEO_CACHE_KEY)

@receiver([post_save, post_delete], sender=Schema)
def clear_schema_cache(sender, **kwargs):
    cache.delete(CONTACT_SCHEMA_CACHE_KEY)

@receiver([post_save, post_delete], sender=ContactTopBar)
def clear_contact_top_bar_cache(sender, **kwargs):
    cache.delete(CONTACT_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=ConatctInfomation)
def clear_conatct_infomation_cache(sender, **kwargs):
    cache.delete(CONTACT_INFOMATION_CACHE_KEY)

@receiver([post_save, post_delete], sender=GoogleMap)
def clear_conatct_google_map_cache(sender, **kwargs):
    cache.delete(CONTACT_GOOGLE_MAP_CACHE_KEY)
