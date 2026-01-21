from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.pages.serializers.pages import PageSerializer
from pages.models import Page
from pages.cache import PAGE_LIST_CACHE_KEY, SINGLE_PAGE_CACHE_KEY, PAGE_CACHE_TIMEOUT

class PageViewSet(APIView):
    def get(self, request, slug=None):
        if slug:
            cache_key = f"{SINGLE_PAGE_CACHE_KEY}:{slug}"
            cached_page = cache.get(cache_key)

            if cached_page:
                return Response(cached_page, status=status.HTTP_200_OK)

            try:
                page = Page.objects.select_related(
                    "seo",
                    "schema",
                    "schema__organization"
                ).get(slug=slug)
            except Page.DoesNotExist:
                return Response(
                    {"detail": "Page not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = PageSerializer(page)
            cache.set(cache_key, serializer.data, PAGE_CACHE_TIMEOUT)

            return Response(serializer.data, status=status.HTTP_200_OK)

        cached_pages = cache.get(PAGE_LIST_CACHE_KEY)
        if cached_pages:
            return Response(cached_pages, status=status.HTTP_200_OK)

        pages = Page.objects.select_related(
            "seo",
            "schema",
            "schema__organization"
        ).all()

        serializer = PageSerializer(pages, many=True)
        cache.set(PAGE_LIST_CACHE_KEY, serializer.data, PAGE_CACHE_TIMEOUT)

        return Response(serializer.data, status=status.HTTP_200_OK)
