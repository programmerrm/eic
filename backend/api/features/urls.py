# ==========================================
"""
FEATURES ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.features.views.features import FeatureViewSet, FeatureItemViewSet

router = DefaultRouter()
router.register(r'title', FeatureViewSet, basename='feature')
router.register(r'items', FeatureItemViewSet, basename='feature-item')

urlpatterns = router.urls
