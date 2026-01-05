from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from faq.cache import FAQ_SEO_CACHE_KEY, FAQ_SCHEMA_CACHE_KEY, FAQ_TOP_BAR_CACHE_KEY, FAQ_SECTION_CACHE_KEY, FAQ_ITEMS_CACHE_KEY
from faq.models import SeoTag, Schema, FaqTopBar, FaqSection, FaqItem

@receiver([pre_save, post_delete], sender=SeoTag)
def clear_faq_seo_cache(sender, **kwargs):
    cache.delete(FAQ_SEO_CACHE_KEY)

@receiver([pre_save, post_delete], sender=Schema)
def clear_faq_schema_cache(sender, **kwargs):
    cache.delete(FAQ_SCHEMA_CACHE_KEY)

@receiver([pre_save, post_delete], sender=FaqTopBar)
def clear_faq_top_bar_cache(sender, **kwargs):
    cache.delete(FAQ_TOP_BAR_CACHE_KEY) 

@receiver([pre_save, post_delete], sender=FaqSection)
def clear_faq_section_cache(sender, **kwargs):
    cache.delete(FAQ_SECTION_CACHE_KEY)

@receiver([pre_save, post_delete], sender=FaqItem)
def clear_faq_items_cache(sender, **kwargs):
    cache.delete(FAQ_ITEMS_CACHE_KEY)

