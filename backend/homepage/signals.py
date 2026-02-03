from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from homepage.models import (
    Banner,
    PaymnetInfo,
    SecurityFirm,
    CybersecuritySolutionItem,
    CybersecuritySolutionTitle,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    ReviewTopBar,
    Review,
    GloballyAccredited,
    ExperienceEic,
    ExperienceEicItem,
)
from homepage.cache import (
    HOMEPAGE_BANNER_CACHE_KEY,
    HOMEPAGE_CYBER_SECURITY_SOLUTION_ITEM_CACHE_KEY,
    HOMEPAGE_CYBER_SECURITY_SOLUTION_TITLE_CACHE_KEY,
    HOMEPAGE_EXPERIENCE_EIC_CACHE_KEY,
    HOMEPAGE_EXPERIENCE_EIC_ITEMS_CACHE_KEY,
    HOMEPAGE_GLOBALLY_ACCREDITED_CACHE_KEY,
    HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_CACHE_KEY,
    HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_ITEMS_CACHE_KEY,
    HOMEPAGE_PAYMNET_INFO_CACHE_KEY,
    HOMEPAGE_REVIEW_CACHE_KEY,
    HOMEPAGE_REVIEW_TOP_BAR_CACHE_KEY,
    HOMEPAGE_SECURITY_FIRM_CACHE_KEY,
)

def cache_clear(key):
    cache.delete(key)

@receiver([post_save, post_delete], sender=Banner)
def banner_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_BANNER_CACHE_KEY)

@receiver([post_save, post_delete], sender=PaymnetInfo)
def paymnet_info_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_PAYMNET_INFO_CACHE_KEY)

@receiver([post_save, post_delete], sender=SecurityFirm)
def security_firm_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_SECURITY_FIRM_CACHE_KEY)

@receiver([post_save, post_delete], sender=CybersecuritySolutionItem)
def cyber_security_solution_item_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_CYBER_SECURITY_SOLUTION_ITEM_CACHE_KEY)

@receiver([post_save, post_delete], sender=CybersecuritySolutionTitle)
def cyber_security_solution_title_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_CYBER_SECURITY_SOLUTION_TITLE_CACHE_KEY)

@receiver([post_save, post_delete], sender=OurProvenProcessSecurity)
def our_proven_process_security_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_CACHE_KEY)

@receiver([post_save, post_delete], sender=OurProvenProcessSecurityItems)
def our_proven_process_security_items_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_ITEMS_CACHE_KEY)

@receiver([post_save, post_delete], sender=ReviewTopBar)
def review_top_bar_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_REVIEW_TOP_BAR_CACHE_KEY)

@receiver([post_save, post_delete], sender=Review)
def review_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_REVIEW_CACHE_KEY)

@receiver([post_save, post_delete], sender=GloballyAccredited)
def globally_accredited_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_GLOBALLY_ACCREDITED_CACHE_KEY)

@receiver([post_save, post_delete], sender=ExperienceEic)
def experience_eic_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_EXPERIENCE_EIC_CACHE_KEY)

@receiver([post_save, post_delete], sender=ExperienceEicItem)
def experience_eic_items_cache_clear(sender, **kwargs):
    cache_clear(HOMEPAGE_EXPERIENCE_EIC_ITEMS_CACHE_KEY)
