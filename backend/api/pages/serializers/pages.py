from rest_framework import serializers
from pages.models import Schema, SeoTag, Organization, Page

class SeoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoTag
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class SchemaSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    schema = serializers.SerializerMethodField()

    class Meta:
        model = Schema
        fields = (
            "id",
            "name",
            "url",
            "description",
            "organization",
            "schema",
        )

    def get_schema(self, obj):
        return obj.json_ld()

class PageSerializer(serializers.ModelSerializer):
    seo = SeoTagSerializer(read_only=True)
    schema = SchemaSerializer(read_only=True)

    class Meta:
        model = Page
        fields = (
            "id",
            "name",
            "slug",
            "seo",
            "schema",
        )
