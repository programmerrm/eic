from rest_framework import serializers
from about_page.models import AboutTopBar, SecureFutureTopBar, SecureFutureItem, SecurityFirm, DigitalSecuritySolutionTopBar, DigitalSecuritySolutionItem, HappyJourneyTopBar, HappyJourneyItem

class AboutTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTopBar
        fields = ['id', 'title', 'description']

class SecureFutureTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFutureTopBar
        fields = ['id', 'normal_title', 'title_span']

class SecureFutureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFutureItem
        fields = ['id', 'title', 'image', 'alt', 'description']

class SecurityFirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityFirm
        fields = ['id', 'bg', 'bg_image_alt', 'main_img', 'main_image_alt', 'title_span', 'title_normal', 'mission_title', 'mission_description', 'vision_title', 'vision_description', 'get_to_know_us_btn_name', 'get_to_know_us_btn_url']

class DigitalSecuritySolutionTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSecuritySolutionTopBar
        fields = ['id', 'title', 'description']

class DigitalSecuritySolutionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSecuritySolutionItem
        fields = ['id', 'count', 'title', 'description']

class HappyJourneyTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyJourneyTopBar
        fields = ['id', 'title']

class HappyJourneyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyJourneyItem
        fields = ['id', 'year', 'title', 'description']
