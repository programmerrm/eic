# ======================================
"""
BLOGS ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from blogs.models import BlogTopBar, Blog, Tag

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
