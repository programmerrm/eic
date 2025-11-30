# ======================================
"""
CONFIGURATION ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from configuration.models import (
    Favicon,
    Logo,
    CopyRight,
    SocialLink,
    NotFoundContent,
    StayCompliant,
    ComplianceTitle,
    ComplianceItem,
    ComplianceItemList,
    Subscribe,
    ScheduleACall,
)

# ============ FAVICON SERIALIZER ===============
class FaviconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favicon
        fields = '__all__'

# ============ LOGO SERIALIZER ===============
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

# ============ COPYRIGHT SERIALIZER ===============
class CopyRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRight
        fields = '__all__'

# ============ SOCIAL LINK SERIALIZER ===============
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

# ============== NOT FOUND CONTENT ==================
class NotFoundContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotFoundContent
        fields = '__all__'

# ============ Stay Compliant ===============
class StayCompliantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayCompliant
        fields = '__all__'

# ============ Compliance Title ===============
class ComplianceTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceTitle
        fields = '__all__'

# ========== Compliance Item List ===============
class ComplianceItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceItemList
        fields = '__all__'

# ========== Compliance Item ================
class ComplianceItemSeriliazer(serializers.ModelSerializer):
    item_list = ComplianceItemListSerializer(many=True, read_only=True)
    class Meta:
        model = ComplianceItem
        fields = '__all__'

# ============= Subscribe ===============
class SubscribeSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

class ScheduleACallSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleACall
        fields = '__all__'
        