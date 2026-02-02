from rest_framework import serializers
from about_page.models import AboutTopBar, SecureFutureTopBar, SecureFutureItem, SecurityFirm, DigitalSecuritySolutionTopBar, DigitalSecuritySolutionItem, HappyJourneyTopBar, HappyJourneyItem

class AboutTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTopBar
        fields = '__all__'

class SecureFutureTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFutureTopBar
        fields = '__all__'

class SecureFutureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFutureItem
        fields = '__all__'

class SecurityFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityFirm
        fields = '__all__'

class DigitalSecuritySolutionTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSecuritySolutionTopBar
        fields = '__all__'

class DigitalSecuritySolutionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSecuritySolutionItem
        fields = '__all__'

class HappyJourneyTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyJourneyTopBar
        fields = '__all__'

class HappyJourneyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyJourneyItem
        fields = '__all__'
