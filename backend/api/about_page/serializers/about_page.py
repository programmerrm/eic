from rest_framework import serializers
from about_page.models import AboutTopBar

class AboutTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTopBar
        fields = '__all__'
