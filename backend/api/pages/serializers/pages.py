# =============================================
"""
PAGES ALL SERIALIZERS
"""
# =============================================
from rest_framework import serializers
from pages.models import (
    Pages,
    SEOKeyword,
    OpenGraphMetaTags,
    TwitterCardMetaTags,
    AdditionalSEOFields,
)

# ============= SEO KEYWORD SERIALIZER ===============
class SEOKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOKeyword
        fields = '__all__'

# ============= OPEN GRAPH META TAGS SERIALIZER ===============
class OpenGraphMetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenGraphMetaTags
        fields = '__all__'

# ============= TWITTER CARD META TAGS SERIALIZER ===============
class TwitterCardMetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterCardMetaTags
        fields = '__all__'

# ============= ADDITIONAL SEO FIELDS SERIALIZER ===============
class AdditionalSEOFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalSEOFields
        fields = '__all__'

# ============= PAGES SERIALIZER ===============
class PagesSerilizer(serializers.ModelSerializer):
    seo_keywords = SEOKeywordSerializer(many=True, read_only=True)
    og_meta = OpenGraphMetaTagsSerializer(read_only=True)
    twitter_meta = TwitterCardMetaTagsSerializer(read_only=True)
    additional_seo = AdditionalSEOFieldsSerializer(read_only=True)
    class Meta:
        model = Pages
        fields = [
            'id', 'name', 'slug', 'content', 'seo_title', 'seo_description',
            'seo_keywords', 'seo_canonical', 'seo_author', 'og_meta',
            'twitter_meta', 'additional_seo'
        ]
