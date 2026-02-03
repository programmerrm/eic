from django.dispatch import receiver
from django.core.cache import cache
from django.db.models.signals import (
    post_save, 
    post_delete,
)
from about_page.models import (
    SecureFutureItem,
    SecureFutureTopBar,
    SecurityFirm,
    HappyJourneyItem,
    HappyJourneyTopBar,
    DigitalSecuritySolutionItem,
    DigitalSecuritySolutionTopBar,
    AboutTopBar,
)
from about_page.cache import (
    ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY,
    ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY,
    ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY,
    ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY,
    ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY,
    ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY,
    ABOUT_SECURITY_FIRM_CACHE_KEY,
    ABOUT_TOP_BAR_CACHE_KEY,
)

def cache_clear(key):
    cache.delete(key)

@receiver([post_save, post_delete], sender=SecureFutureItem)
def clear_secure_future_items_cache(sender, **kwargs):
    cache_clear(ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY)

@receiver([post_save, post_delete], sender=SecureFutureTopBar)
def clear_secure_future_top_bar_cache(sender, **kwargs):
    cache_clear(ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=HappyJourneyItem)
def clear_happy_journey_items_cache(sender, **kwargs):
    cache_clear(ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY)

@receiver([post_save, post_delete], sender=HappyJourneyTopBar)
def clear_happy_journey_top_bar_cache(sender, **kwargs):
    cache_clear(ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=DigitalSecuritySolutionItem)
def clear_digital_security_solution_items_cache(sender, **kwargs):
    cache_clear(ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY)

@receiver([post_save, post_delete], sender=DigitalSecuritySolutionTopBar)
def clear_digital_security_solution_top_bar_cache(sender, **kwargs):
    cache_clear(ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=SecurityFirm)
def clear_security_firm_cache(sender, **kwargs):
    cache_clear(ABOUT_SECURITY_FIRM_CACHE_KEY)

@receiver([post_save, post_delete], sender=AboutTopBar)
def clear_about_top_bar_cache(sender, **kwargs):
    cache_clear(ABOUT_TOP_BAR_CACHE_KEY)
