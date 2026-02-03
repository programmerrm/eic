######################################################
"""
HOMEPAGE ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from api.homepage.serializers.homepage import (
    BannerSerializer,
    SecurityFirmSerializer, 
    CybersecuritySolutionTitleSerializer,
    CybersecuritySolutionItemSerializer,
    OurProvenProcessSecuritySerializer,
    OurProvenProcessSecurityItemsSerializer,
    PaymnetInfoSerializer,
    ReviewTopBarSerializer,
    ReviewSerializer,
    ExperienceEicSerializer,
    ExperienceEicItemSerializer,
    GloballyAccreditedSerializer,
)
from homepage.models import (
    Banner,
    SecurityFirm,
    CybersecuritySolutionTitle,
    CybersecuritySolutionItem,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    PaymnetInfo,
    ReviewTopBar,
    Review,
    ExperienceEic,
    ExperienceEicItem,
    GloballyAccredited,
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
    CACHE_TIME_OUT,
)
from api.configuration.views.base import (
    BaseRetrieveView,
    BaseListView,
)

# =========== BANNER VIEW SET =============
class BannerViewSet(BaseRetrieveView):
    serializer_class = BannerSerializer
    CACHE_KEY = HOMEPAGE_BANNER_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = BannerSerializer.Meta.fields
        return Banner.objects.only(*fields)

# =========== Paymnet Info VIEW SET =============
class PaymnetInfoViewSet(BaseRetrieveView):
    serializer_class = PaymnetInfoSerializer
    CACHE_KEY = HOMEPAGE_PAYMNET_INFO_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = PaymnetInfoSerializer.Meta.fields
        return PaymnetInfo.objects.only(*fields)

# =========== SECURITY FIRM VIEW SET =============
class SecurityFirmViewSet(BaseRetrieveView):
    serializer_class = SecurityFirmSerializer
    CACHE_KEY = HOMEPAGE_SECURITY_FIRM_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = SecurityFirmSerializer.Meta.fields
        return SecurityFirm.objects.only(*fields)

# ========= Cyber Security Solution Title View Set ============
class CybersecuritySolutionTitleViewSet(BaseRetrieveView):
    serializer_class = CybersecuritySolutionTitleSerializer
    CACHE_KEY = HOMEPAGE_CYBER_SECURITY_SOLUTION_TITLE_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = CybersecuritySolutionTitleSerializer.Meta.fields
        return CybersecuritySolutionTitle.objects.only(*fields)

# ======== Cyber Security Solution Item View Set ========
class CybersecuritySolutionItemViewSet(BaseListView):
    serializer_class = CybersecuritySolutionItemSerializer
    CACHE_KEY = HOMEPAGE_CYBER_SECURITY_SOLUTION_ITEM_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_queryset_instance(self):
        fields = CybersecuritySolutionItemSerializer.Meta.fields
        return CybersecuritySolutionItem.objects.only(*fields)

# ========= Our Proven Process Security View Set ========
class OurProvenProcessSecurityViewSet(BaseRetrieveView):
    serializer_class = OurProvenProcessSecuritySerializer
    CACHE_KEY = HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = OurProvenProcessSecuritySerializer.Meta.fields
        return OurProvenProcessSecurity.objects.only(*fields)
    
# ========= Our Proven Process Security Items View Set =======
class OurProvenProcessSecurityItemsViewSet(BaseListView):
    serializer_class = OurProvenProcessSecurityItemsSerializer
    CACHE_KEY = HOMEPAGE_OUR_PROVEN_PROCESS_SECURITY_ITEMS_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_queryset_instance(self):
        fields = OurProvenProcessSecurityItemsSerializer.Meta.fields
        return OurProvenProcessSecurityItems.objects.only(*fields)

# ======= ReviewTopBarViewSet ===========
class ReviewTopBarViewSet(BaseRetrieveView):
    serializer_class = ReviewTopBarSerializer
    CACHE_KEY = HOMEPAGE_REVIEW_TOP_BAR_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = ReviewTopBarSerializer.Meta.fields
        return ReviewTopBar.objects.only(*fields)

# =========== Review View Set ===========
class ReviewViewSet(BaseListView):
    serializer_class = ReviewSerializer
    CACHE_KEY = HOMEPAGE_REVIEW_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_queryset_instance(self):
        fields = ReviewSerializer.Meta.fields
        return Review.objects.only(*fields)

# ========== Experience Eic View Set ===========
class ExperienceEicViewSet(BaseRetrieveView):
    serializer_class = ExperienceEicSerializer
    CACHE_KEY = HOMEPAGE_EXPERIENCE_EIC_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = ExperienceEicSerializer.Meta.fields
        return ExperienceEic.objects.only(*fields)

# ======== Experience Eic Item View Set ==========
class ExperienceEicItemViewSet(BaseListView):
    serializer_class = ExperienceEicItemSerializer
    CACHE_KEY = HOMEPAGE_EXPERIENCE_EIC_ITEMS_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_queryset_instance(self):
        fields = ExperienceEicItemSerializer.Meta.fields
        return ExperienceEicItem.objects.only(*fields)

# ======== Globally Accredited View Set =========
class GloballyAccreditedViewSet(BaseRetrieveView):
    serializer_class = GloballyAccreditedSerializer
    CACHE_KEY = HOMEPAGE_GLOBALLY_ACCREDITED_CACHE_KEY
    CACHE_TIMEOUT = CACHE_TIME_OUT

    def get_object_instance(self):
        fields = GloballyAccreditedSerializer.Meta.fields
        return GloballyAccredited.objects.only(*fields)
