# ==========================================
"""
ABOUT ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.about_page.views.about_page import (
    AboutTopBarView,
    SecureFutureTopBarView,
    SecureFutureItemView,
    SecurityFirmView,
    DigitalSecuritySolutionTopBarView,
    DigitalSecuritySolutionItemView,
    HappyJourneyTopBarView,
    HappyJourneyItemView,
    SchemaView,
    SeoTagView
)

router = DefaultRouter()
router.register(r'seo-tag', SeoTagView, basename='aboutpage_seo_tag')
router.register(r'schema', SchemaView, basename='aboutpage_schema')
router.register(r'top-bar', AboutTopBarView, basename='about_top_bar')
router.register(r'secure-future-top-bar', SecureFutureTopBarView, basename='about_secure_futurea_top_bar')
router.register(r'secure-future-item', SecureFutureItemView, basename='about_secure_future_item_view')
router.register(r'security-firm', SecurityFirmView, basename='about_security_firm_view')
router.register(r'digital-security-solution-top-bar', DigitalSecuritySolutionTopBarView, basename='about_digital_security_solution_top_bar')
router.register(r'digital-security-solution-item', DigitalSecuritySolutionItemView, basename='about_digital_security_solution_item')
router.register(r'happy-journey', HappyJourneyTopBarView, basename='about_happy_journey_top_bar')
router.register(r'happy-journey-item', HappyJourneyItemView, basename='about_happy_journey_item')

urlpatterns = router.urls
