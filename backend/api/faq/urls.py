from rest_framework.routers import DefaultRouter
from api.faq.views.faq import (
    FaqItemView, 
    FaqSectionView, 
    FaqTopBarView, 
    SchemaViewSet, 
    SeoTagViewSet,
)

router = DefaultRouter()
router.register(r'item-list', FaqItemView, basename='faq_item_list')
router.register(r'section', FaqSectionView, basename='faq_section')
router.register(r'top-bar', FaqTopBarView, basename='faq_top_bar')
router.register(r'schema', SchemaViewSet, basename='faq_schema')
router.register(r'seo-tag', SeoTagViewSet, basename='faq_seo_tag')

urlpatterns = router.urls
