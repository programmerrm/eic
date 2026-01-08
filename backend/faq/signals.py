from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from faq.cache import FAQ_SEO_CACHE_KEY, FAQ_SCHEMA_CACHE_KEY, FAQ_TOP_BAR_CACHE_KEY, FAQ_SECTION_CACHE_KEY, FAQ_ITEMS_CACHE_KEY
from faq.models import SeoTag, Schema, FaqTopBar, FaqSection, FaqItem
from utils.trigger_nextjs_revalidate import trigger_nextjs_revalidate

@receiver([pre_save, post_delete], sender=SeoTag)
def clear_faq_seo_cache(sender, **kwargs):
    cache.delete(FAQ_SEO_CACHE_KEY)
    trigger_nextjs_revalidate(
        path="/faq/seo-tag/",
        tag="faq-seo"
    )

@receiver([pre_save, post_delete], sender=Schema)
def clear_faq_schema_cache(sender, **kwargs):
    cache.delete(FAQ_SCHEMA_CACHE_KEY)
    trigger_nextjs_revalidate(
        path="/faq/schema/",
        tag="faq-schema"
    )

@receiver([pre_save, post_delete], sender=FaqTopBar)
def clear_faq_top_bar_cache(sender, **kwargs):
    print("[Signal] FaqTopBar changed! Clearing cache and triggering Next.js revalidate...")  # ✅ print

    cache.delete(FAQ_TOP_BAR_CACHE_KEY)

    success = trigger_nextjs_revalidate(
        path="/faq/top-bar/",
        tag="faq-top-bar"
    )

    print(f"[Signal] Next.js revalidate success: {success}")  # ✅ print response


@receiver([pre_save, post_delete], sender=FaqSection)
def clear_faq_section_cache(sender, **kwargs):
    cache.delete(FAQ_SECTION_CACHE_KEY)
    trigger_nextjs_revalidate(
        path="/faq/section/",
        tag="faq-section"
    )

@receiver([pre_save, post_delete], sender=FaqItem)
def clear_faq_items_cache(sender, **kwargs):
    cache.delete(FAQ_ITEMS_CACHE_KEY)
    trigger_nextjs_revalidate(
        path="/faq/item-list/",
        tag="faq-item-list"
    )
