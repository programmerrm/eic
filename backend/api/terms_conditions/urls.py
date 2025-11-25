# ==========================================
"""
TERMS CONDITIONS ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from .views.terms_conditions import TermsConditionTopBarView, TermsConditionContentView

router = DefaultRouter()
router.register(r'terms-condition-top-bar', TermsConditionTopBarView, basename='terms_condition_top_bar')
router.register(r'terms-condition-content', TermsConditionContentView, basename='terms_condition_content')

urlpatterns = router.urls
