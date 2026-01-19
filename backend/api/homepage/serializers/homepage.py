# ======================================
"""
HOMEPAGE ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from homepage.models import (
    Banner,
    PaymnetInfo,
    SecurityFirm, 
    CybersecuritySolutionItem, 
    CybersecuritySolutionTitle,
    OurProvenProcessSecurity,
    OurProvenProcessSecurityItems,
    ReviewTopBar,
    Review,
    ExperienceEic,
    ExperienceEicItem,
    GloballyAccredited,
    Organization,
    HomePageSchema,
    SeoTag,
)

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__' 

class SchemaSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    schema = serializers.SerializerMethodField()

    class Meta:
        model = HomePageSchema
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

# =========== Seo Tag =================
class SeoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoTag
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


# ============ BANNER SERIALIZER ===============
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# =========== Paymnet Info Serializer ==============
class PaymnetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymnetInfo
        fields = '__all__'

# ============ SECURITY FIRM SERIALIZER ===============
class SecurityFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityFirm
        fields = '__all__'

# ============= Cyber Security Solution Title ==========
class CybersecuritySolutionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecuritySolutionTitle
        fields = '__all__'

# ============= Cyber Security Solution Item ==============
class CybersecuritySolutionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecuritySolutionItem
        fields = '__all__'

# =============== Our Proven Process Security ==============
class OurProvenProcessSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProvenProcessSecurity
        fields = '__all__'

# ============= Our Proven Process Security Items =============
class OurProvenProcessSecurityItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProvenProcessSecurityItems
        fields = '__all__'

# ============== Review Top Bar ===============
class ReviewTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTopBar
        fields = '__all__'

# =========== REVIEW ==============
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# ========== ExperienceEic ===========
class ExperienceEicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEic
        fields = '__all__'

# ============= Experience Eic Item ==============
class ExperienceEicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEicItem
        fields = '__all__'

# ============= Globally Accredited =============
class GloballyAccreditedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GloballyAccredited
        fields = '__all__'
