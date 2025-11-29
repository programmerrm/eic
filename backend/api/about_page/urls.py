# ==========================================
"""
ABOUT ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.about_page.views.about_page import AboutTopBarView

router = DefaultRouter()
router.register(r'top-bar', AboutTopBarView, basename='blog_top_bar')

urlpatterns = router.urls
