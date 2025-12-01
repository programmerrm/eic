from rest_framework import serializers
from faq.models import FaqTopBar, FaqSection, FaqItem, Schema, SeoTag

class FaqTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqTopBar
        fields = '__all__'

class FaqSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqSection
        fields = '__all__'

class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqItem
        fields = '__all__'

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
