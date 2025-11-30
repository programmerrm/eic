from rest_framework import serializers
from faq.models import FaqTopBar, FaqSection, FaqItem

class FaqTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqTopBar
        fields = '__all__'

class FaqSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqSection
        fields = '__all__'

class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqItem
        fields = '__all__'
