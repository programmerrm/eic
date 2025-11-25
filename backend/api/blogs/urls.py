# ==========================================
"""
BLOG ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.blogs.views.blogs import BlogTopBarView, BlogView, SingleBlogView, SeoTagView, SchemaView

router = DefaultRouter()
router.register(r'seo-tag', SeoTagView, basename='seo_tag')
router.register(r'schema', SchemaView, basename='schema_view')
router.register(r'top-bar', BlogTopBarView, basename='blog_top_bar')
router.register(r'list', BlogView, basename='all_blogs')
router.register(r'single', SingleBlogView, basename='single_blog')

urlpatterns = router.urls
