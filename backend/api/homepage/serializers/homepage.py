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
)

# ============ BANNER SERIALIZER ===============
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'alt', 'title', 'description', 'secure_business_btn_name', 'secure_business_btn_url', 'company_profile_btn_name', 'company_profile_btn_url']

# =========== Paymnet Info Serializer ==============
class PaymnetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymnetInfo
        fields = ['id', 'image', 'alt', 'title_before_span', 'title_span', 'title_after_span', 'description', 'btn_name', 'btn_url']

# ============ SECURITY FIRM SERIALIZER ===============
class SecurityFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityFirm
        fields = ['id', 'bg', 'main_img', 'main_img_alt', 'sub_img', 'sub_img_alt', 'title_span', 'title_normal', 'mission_title', 'mission_description', 'vision_title', 'vision_description', 'get_to_know_us_btn_name', 'get_to_know_us_btn_url', 'security_persentences', 'response_persentences', 'compliance_persentences']

# ============= Cyber Security Solution Title ==========
class CybersecuritySolutionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecuritySolutionTitle
        fields = ['id', 'title', 'description', 'image', 'alt']

# ============= Cyber Security Solution Item ==============
class CybersecuritySolutionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecuritySolutionItem
        fields = ['id', 'image', 'alt', 'title', 'count']

# =============== Our Proven Process Security ==============
class OurProvenProcessSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProvenProcessSecurity
        fields = ['id', 'image', 'alt', 'title_before_span', 'title_span', 'title_after_span', 'description']

# ============= Our Proven Process Security Items =============
class OurProvenProcessSecurityItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProvenProcessSecurityItems
        fields = ['id', 'image', 'alt', 'title', 'description']

# ============== Review Top Bar ===============
class ReviewTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTopBar
        fields = ['id', 'title_before_span', 'title_span', 'title_after_span']

# =========== REVIEW ==============
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author_image', 'author_name', 'author_bio', 'content']

# ========== ExperienceEic ===========
class ExperienceEicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEic
        fields = ['id', 'normal_title', 'span_title', 'image', 'alt', 'btn_name', 'btn_url']

# ============= Experience Eic Item ==============
class ExperienceEicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEicItem
        fields = ['id', 'name']

# ============= Globally Accredited =============
class GloballyAccreditedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GloballyAccredited
        fields = ['id', 'title', 'image', 'alt', 'bg']
