# ==========================================
"""
PRIVACY POLICY ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from .views.privacy_policy import PrivacyPolicyTopBarView, PrivacyPolicyContentView

router = DefaultRouter()
router.register(r'privacy-policy-top-bar', PrivacyPolicyTopBarView, basename='privacy_policy_top_bar')
router.register(r'privacy-policy-content', PrivacyPolicyContentView, basename='privacy_policy_content')

urlpatterns = router.urls