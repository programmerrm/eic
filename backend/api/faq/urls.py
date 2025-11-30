from rest_framework.routers import DefaultRouter
from api.faq.views.faq import FaqItemView, FaqSectionView, FaqTopBarView

router = DefaultRouter()
router.register(r'item-list', FaqItemView, basename='faq_item_list')
router.register(r'section', FaqSectionView, basename='faq_section')
router.register(r'top-bar', FaqTopBarView, basename='faq_top_bar')

urlpatterns = router.urls
