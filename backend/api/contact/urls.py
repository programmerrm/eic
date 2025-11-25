# ==========================================
"""
CONTACT ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.contact.views.contact import ContactTopBarView, ContactFormView, ConatctInfomationView, GoogleMapView, SeoTagView, SchemaView

router = DefaultRouter()
router.register(r'seo-tag', SeoTagView, basename='seo_tag')
router.register(r'schema', SchemaView, basename='schema_view')
router.register(r'top-bar', ContactTopBarView, basename='top_bar')
router.register(r'form-create', ContactFormView, basename='form_create')
router.register(r'infomation', ConatctInfomationView, basename='infomation')
router.register(r'google-map', GoogleMapView, basename='google_map')

urlpatterns = router.urls
