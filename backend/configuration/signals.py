################################################
"""
CONFIGRATION SIGNALS HERE.
"""
################################################
from django.dispatch import receiver
from django.core.cache import cache
from django.db.models.signals import (
    post_save, 
    post_delete,
)
from configuration.cache import (
    FAVICON_CACHE_KEY,
    LOGO_CACHE_KEY,
    COPY_RIGHT_CACHE_KEY,
    SOCIAL_LINK_CACHE_KEY,
    NOT_FOUND_CONTENT_CACHE_KEY,
    STAY_COMPLIANT_CACHE_KEY,
    SCHEDULE_A_CALL_CACHE_KEY,
    COMPLIANCE_ITEMS_CACHE_KEY,
    COMPLIANCE_ITEMS_LIST_CACHE_KEY,
    COMPLIANCE_TITLE_CACHE_KEY,
)
from configuration.models import (
    Favicon,
    Logo,
    CopyRight,
    ScheduleACall,
    SocialLink,
    StayCompliant,
    NotFoundContent,
    ComplianceTitle,
    ComplianceItem,
    ComplianceItemList
)

@receiver([post_save, post_delete], sender=Favicon)
def clear_favicon_cache(sender, **kwargs):
    cache.delete(FAVICON_CACHE_KEY)

@receiver([post_save, post_delete], sender=Logo)
def clear_logo_cache(sender, **kwargs):
    cache.delete(LOGO_CACHE_KEY)

@receiver([post_save, post_delete], sender=CopyRight)
def clear_copy_right_cache(sender, **kwargs):
    cache.delete(COPY_RIGHT_CACHE_KEY)

@receiver([post_save, post_delete], sender=SocialLink)
def clear_social_link_cache(sender, **kwargs):
    cache.delete(SOCIAL_LINK_CACHE_KEY)

@receiver([post_save, post_delete], sender=NotFoundContent)
def clear_not_found_content_cache(sender, **kwargs):
    cache.delete(NOT_FOUND_CONTENT_CACHE_KEY)

@receiver([post_save, post_delete], sender=StayCompliant)
def clear_stay_compliant_cache(sender, **kwargs):
    cache.delete(STAY_COMPLIANT_CACHE_KEY)

@receiver([post_save, post_delete], sender=ScheduleACall)
def clear_schedule_a_call_cache(sender, **kwargs):
    cache.delete(SCHEDULE_A_CALL_CACHE_KEY)

@receiver([post_save, post_delete], sender=ComplianceTitle)
def clear_compliance_title_cache(sender, **kwargs):
    cache.delete(COMPLIANCE_TITLE_CACHE_KEY)

@receiver([post_save, post_delete], sender=ComplianceItem)
def clear_compliance_items_cache(sender, **kwargs):
    cache.delete(COMPLIANCE_ITEMS_CACHE_KEY)

@receiver([post_save, post_delete], sender=ComplianceItemList)
def clear_compliance_items_list_cache(sender, **kwargs):
    cache.delete(COMPLIANCE_ITEMS_LIST_CACHE_KEY)
