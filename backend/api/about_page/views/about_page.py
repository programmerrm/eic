from api.about_page.serializers.about_page import (
    AboutTopBarSerializer,
    SecureFutureItemSerializer,
    SecureFutureTopBarSerializer,
    SecurityFirmSerializer,
    DigitalSecuritySolutionTopBarSerializer,
    DigitalSecuritySolutionItemSerializer,
    HappyJourneyTopBarSerializer,
    HappyJourneyItemSerializer,
)
from about_page.models import (
    AboutTopBar, 
    SecureFutureTopBar, 
    SecureFutureItem,
    SecurityFirm,
    DigitalSecuritySolutionTopBar,
    DigitalSecuritySolutionItem,
    HappyJourneyTopBar,
    HappyJourneyItem,
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
    PAGE_CACHE_TIMEOUT,
)
from api.configuration.views.base import (
    BaseRetrieveView, 
    BaseListView,
)

# ============ About Top Bar  ===============
class AboutTopBarView(BaseRetrieveView):
    serializer_class = AboutTopBarSerializer
    CACHE_KEY = ABOUT_TOP_BAR_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_object_instance(self):
        fields = AboutTopBarSerializer.Meta.fields
        return AboutTopBar.objects.only(*fields)
    
# ========== Secure Future Top Bar ============
class SecureFutureTopBarView(BaseRetrieveView):
    serializer_class = SecureFutureTopBarSerializer
    CACHE_KEY = ABOUT_SECURE_FUTURE_TOP_BAR_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_object_instance(self):
        fields = SecureFutureTopBarSerializer.Meta.fields
        return SecureFutureTopBar.objects.only(*fields)
    
# =========== Secure Future Items =============
class SecureFutureItemView(BaseListView):
    serializer_class = SecureFutureItemSerializer
    CACHE_KEY = ABOUT_SECURE_FUTURE_ITEMS_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_queryset_instance(self):
        fields = SecureFutureItemSerializer.Meta.fields
        return SecureFutureItem.objects.only(*fields)

# =============== Security Firm =================
class SecurityFirmView(BaseRetrieveView):
    serializer_class = SecurityFirmSerializer
    CACHE_KEY = ABOUT_SECURITY_FIRM_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_object_instance(self):
        fields = SecurityFirmSerializer.Meta.fields
        return SecurityFirm.objects.only(*fields)

# =========== Digital Security Solution Top Bar ==========
class DigitalSecuritySolutionTopBarView(BaseRetrieveView):
    serializer_class = DigitalSecuritySolutionTopBarSerializer
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_TOP_BAR_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT
    
    def get_object_instance(self):
        fields = DigitalSecuritySolutionTopBarSerializer.Meta.fields
        return DigitalSecuritySolutionTopBar.objects.only(*fields)
        
# ============ Digital Security Solution Items =============
class DigitalSecuritySolutionItemView(BaseListView):
    serializer_class = DigitalSecuritySolutionItemSerializer
    CACHE_KEY = ABOUT_DIGITAL_SECURITY_SOLUTION_ITEMS_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_queryset_instance(self):
        fields = DigitalSecuritySolutionItemSerializer.Meta.fields
        return DigitalSecuritySolutionItem.objects.only(*fields)

# ============ Happy Journey Top Bar ============
class HappyJourneyTopBarView(BaseRetrieveView):
    serializer_class = HappyJourneyTopBarSerializer
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_TOP_BAR_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_object_instance(self):
        fields = HappyJourneyTopBarSerializer.Meta.fields
        return HappyJourneyTopBar.objects.only(*fields)

# ============== Happy Journey Items ==============
class HappyJourneyItemView(BaseListView):
    serializer_class = HappyJourneyItemSerializer
    CACHE_KEY = ABOUT_HAPPY_JOURNEY_ITEMS_CACHE_KEY
    CACHE_TIMEOUT = PAGE_CACHE_TIMEOUT

    def get_queryset_instance(self):
        fields = HappyJourneyItemSerializer.Meta.fields
        return HappyJourneyItem.objects.only(*fields)
