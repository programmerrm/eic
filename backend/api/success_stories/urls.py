from rest_framework.routers import DefaultRouter
from api.success_stories.views.success_stories import SuccessStorieTopBarView, SuccessStorieView, SingleSuccessStorieView

router = DefaultRouter()
router.register(r'top-bar', SuccessStorieTopBarView, basename='success_storie_top_bar')
router.register(r'list', SuccessStorieView, basename='all_success_storie')
router.register(r'single', SingleSuccessStorieView, basename='single_success_storie')

urlpatterns = router.urls
