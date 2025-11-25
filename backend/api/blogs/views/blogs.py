######################################################
"""
BLOGS ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from api.blogs.serializers.blogs import BlogTopBarSerializer, BlogSerializer, SingleBlogSerializer, SeoTagSerializer, SchemaSerializer, RelatedBlogSerializer
from blogs.pagination import CumulativePagination
from blogs.models import BlogTopBar, Blog, Schema, SeoTag

# ============= Blog SEO TAGS View =================
class SeoTagView(viewsets.ModelViewSet):
    serializer_class = SeoTagSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = SeoTag.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Blog seo tags records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Blog seo tags data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============= Blog SCHEMA View =================
class SchemaView(viewsets.ModelViewSet):
    serializer_class = SchemaSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = Schema.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Blog schema records not found',
                    'data': {},
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Blog schema data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============ BLOG TOP BAR VIEW ===============
class BlogTopBarView(viewsets.ModelViewSet):
    serializer_class = BlogTopBarSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = BlogTopBar.objects.first()
            if not queryset:
                return Response({
                    'success': False,
                    'message': 'Blog top bar records not found',
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(queryset)
            return Response({
                'success': True,
                'message': 'Blog top bar data fetching successfully.',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ============ BLOG VIEW ===============
class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    pagination_class = CumulativePagination
    queryset = Blog.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response({
                    'success': True,
                    'message': 'Blog data fetched successfully.',
                    'data': serializer.data,
                })
            serializer = self.get_serializer(self.queryset, many=True)
            return Response({
                'success': True,
                'message': 'Blog data fetched successfully.',
                'data': serializer.data,
            })
        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            })
        
# ============ SINGLE BLOG VIEW ===============
class SingleBlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = SingleBlogSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        try:
            blog = self.get_object()
            serializer = self.get_serializer(blog)

            tag_ids = blog.tags.values_list('id', flat=True)

            related_blogs = (
                Blog.objects.filter(tags__in=tag_ids)
                .exclude(id=blog.id)
                .distinct()
                .order_by('-created_at')[:6]
            )
            related_serializer = RelatedBlogSerializer(related_blogs, many=True)

            return Response({
                'success': True,
                'message': 'Single blog fetched successfully.',
                'data': serializer.data,
                'related_blogs': related_serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': 'Something went wrong.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        