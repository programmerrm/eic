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
)

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
