from rest_framework import serializers
from success_stories.models import SuccessStorieTopBar, SuccessStorieCategory, SuccessStorie, Schema, SeoTag

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

class SuccessStorieTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStorieTopBar
        fields = '__all__'
    
class SuccessStorieCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStorieCategory
        fields = '__all__'

class SuccessStorieSerializer(serializers.ModelSerializer):
    categories = SuccessStorieCategorySerializer(many=True, read_only=True)
    class Meta:
        model = SuccessStorie
        fields = '__all__'

class SingleSuccessStorieSerializer(serializers.ModelSerializer):
    categories = SuccessStorieCategorySerializer(many=True, read_only=True)
    related_success_stories = serializers.SerializerMethodField()

    class Meta:
        model = SuccessStorie
        fields = '__all__'

    def get_related_success_stories(self, obj):
        related = SuccessStorie.objects.filter(
            categories__in=obj.categories.all()
        ).exclude(id=obj.id).distinct().order_by('-created_at')[:2]
        return [
            {
                'id': item.id,
                'title': item.title,
                'slug': item.slug,
                'image': item.image.url if item.image else None,
                'budget_description': item.budget_description,
            } for item in related
        ]
    