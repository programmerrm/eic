# ======================================
"""
CONTACT ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from contact.models import ContactTopBar, ContactForm, ConatctInfomation, GoogleMap, SeoTag, Schema

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

# =========== Contact Top Bar =================
class ContactTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTopBar
        fields = '__all__'

# =========== Contact Form =================
class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

# =========== Conatct Infomation =================
class ConatctInfomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConatctInfomation
        fields = '__all__'

# ============ Google Map ===============
class GoogleMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleMap
        fields = '__all__'
        