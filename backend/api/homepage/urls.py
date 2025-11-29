# ==========================================
"""
HOMEPAGE ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.homepage.views.homepage import (
    BannerViewSet,
    PaymnetInfoViewSet,
    SecurityFirmViewSet, 
    CybersecuritySolutionTitleViewSet, 
    CybersecuritySolutionItemViewSet,
    OurProvenProcessSecurityViewSet,
    OurProvenProcessSecurityItemsViewSet,
    ReviewViewSet,
    ReviewTopBarViewSet,
)

router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'paymnet-info', PaymnetInfoViewSet, basename='paymnet_info')
router.register(r'security-firm', SecurityFirmViewSet, basename='security_firm')
router.register(r'cyber-security-solution-title', CybersecuritySolutionTitleViewSet, basename='cyber_security_solution_title')
router.register(r'cyber-security-solution-items', CybersecuritySolutionItemViewSet, basename='cyber_security_solution_items')
router.register(r'our-proven-process-security', OurProvenProcessSecurityViewSet, basename='our_proven_process_security')
router.register(r'our-proven-process-security-items', OurProvenProcessSecurityItemsViewSet, basename='our_proven_process_security_items')
router.register(r'review-top-bar', ReviewTopBarViewSet, basename='review_top_bar')
router.register(r'review-items', ReviewViewSet, basename='review_items')

urlpatterns = router.urls
