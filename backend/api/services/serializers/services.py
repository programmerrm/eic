from rest_framework import serializers
from services.models import ServicePageTopBar, Categories, Service, Faq, FaqItem, ServiceItemMain, ServiceItem, ServicesIncludeTopTitle, ServicesIncludeTopItem, ServicesIncludeBottomTitle, ServicesIncludeBottomItem

class ServicePageTopBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePageTopBar
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class RelatedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

# FAQ Item Serializer
class FaqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqItem
        fields = ['id', 'question', 'answer']

# FAQ Serializer
class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'title', 'image']

class ServiceItemMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMain
        fields = '__all__'

class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = '__all__'

class ServicesIncludeTopTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIncludeTopTitle
        fields = '__all__'

class ServicesIncludeTopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIncludeTopItem
        fields = '__all__'

class ServicesIncludeBottomTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIncludeBottomTitle
        fields = '__all__'

class ServicesIncludeBottomItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesIncludeBottomItem
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    main_item = ServiceItemMainSerializer(read_only=True)
    items = ServiceItemSerializer(many=True, read_only=True)
    include_top_title = ServicesIncludeTopTitleSerializer(read_only=True)
    include_top_items = ServicesIncludeTopItemSerializer(many=True, read_only=True)
    include_bottom_title = ServicesIncludeBottomTitleSerializer(read_only=True)
    include_bottom_items = ServicesIncludeBottomItemSerializer(many=True, read_only=True)
    faqs = FaqSerializer(many=True, read_only=True)
    faq_items = FaqItemSerializer(many=True, read_only=True)
    related_services = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    def get_related_services(self, obj):
        qs = Service.objects.filter(categories__in=obj.categories.all()).exclude(id=obj.id).distinct()
        return RelatedServiceSerializer(qs, many=True, context=self.context).data
