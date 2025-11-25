# ======================================
"""
PRIVACY POLICY ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from privacy_policy.models import PrivacyPolicyTopBar, PrivacyPolicyContent

# ======== PRIVACY POLICY Top Bar =========
class PrivacyPolicyTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyTopBar
        fields = '__all__'

# ======== PRIVACY POLICY Content =========
class PrivacyPolicyContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyContent
        fields = '__all__'
