# ======================================
"""
TERMS CONDITIONS ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from terms_conditions.models import TermsConditionTopBar, TermsConditionContent

# ======== Terms Condition Top Bar =========
class TermsConditionTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsConditionTopBar
        fields = '__all__'

# ======== Terms Condition Content =========
class TermsConditionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsConditionContent
        fields = '__all__'
