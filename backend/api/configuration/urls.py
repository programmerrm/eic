# ==========================================
"""
CONFIGURATION ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.configuration.views.configuration import (
    FaviconViewSet,
    LogoViewSet,
    CopyRightViewSet,
    SocialLinkViewSet,
    NotFoundContentViewSet,
    StayCompliantView,
    ComplianceTitleView,
    ComplianceItemView,
)

router = DefaultRouter()
router.register(r'favicon', FaviconViewSet, basename='favicon')
router.register(r'logo', LogoViewSet, basename='logo')
router.register(r'copy-right', CopyRightViewSet, basename='copy_right')
router.register(r'social-link', SocialLinkViewSet, basename='social_link')
router.register(r'not-found-content', NotFoundContentViewSet, basename='not_found_content')
router.register(r'stay-compliant', StayCompliantView, basename='stay_compliant')
router.register(r'compliance-title', ComplianceTitleView, basename='compliance_title')
router.register(r'compliance-item', ComplianceItemView, basename='compliance_item')

urlpatterns = router.urls
