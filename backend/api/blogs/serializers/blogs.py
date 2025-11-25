# ======================================
"""
BLOGS ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from blogs.models import BlogTopBar, Blog, Tag, SeoTag, Schema

# =========== Seo Tag =================
class SeoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoTag
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# =========== Schema =================
class SchemaSerializer(serializers.ModelSerializer):
    json_ld = serializers.SerializerMethodField()

    class Meta:
        model = Schema
        fields = '__all__'

    def get_json_ld(self, obj):
        return obj.json_ld()

# ================= BLOG TOP BAR =================
class BlogTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTopBar
        fields = '__all__'

# ================= TAG =================
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# ========= SINGLE BLOG ================
class SingleBlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'content',
            'author_image',
            'author_name',
            'author_bio',
            'author_description',
            'author_facebook_url',
            'author_twitter_url',
            'author_medium_url',
            'created_at',
            'tags',
        ]
        read_only_fields = ['slug', 'created_at']

# ========= Related Blog Serializer ==========
class RelatedBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug']

# ================= BLOG =================
class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'content',
            'author_image',
            'author_name',
            'author_bio',
            'author_description',
            'author_facebook_url',
            'author_twitter_url',
            'author_medium_url',
            'created_at',
            'tags',
        ]
        read_only_fields = ['slug', 'created_at']

