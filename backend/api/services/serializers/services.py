from rest_framework import serializers
from services.models import ServicePageTopBar, Categories, Service, Faq, FaqItem, ServiceItemMain, ServiceItem, ServicesIncludeTopTitle, ServicesIncludeTopItem, ServicesIncludeBottomTitle, ServicesIncludeBottomItem, ServicePaymnet, ServiceWhyChooseUsTitle, ServiceWhyChooseUsItem, SeoTag, Schema, ComplianceTitle, ComplianceItemList, ComplianceItem

# =========== Seo Tag =================
class SeoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoTag
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# =========== Schema =================
class SchemaSerializer(serializers.ModelSerializer):
    json_ld = serializers.SerializerMethodField()

    class Meta:
        model = Schema
        fields = '__all__'

    def get_json_ld(self, obj):
        return obj.json_ld()
    
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
    
    class Meta:
        model = Service
        fields = '__all__'

class ServicePaymnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePaymnet
        fields = '__all__'

class ServiceWhyChooseUsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceWhyChooseUsTitle
        fields = '__all__'

class ServiceWhyChooseUsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceWhyChooseUsItem
        fields = '__all__'

class ComplianceTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceTitle
        fields = '__all__'

class ComplianceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceItem
        fields = '__all__'

class ComplianceItemListSerializer(serializers.ModelSerializer):
    items = ComplianceItemSerializer(many=True, read_only=True)
    class Meta:
        model = ComplianceItemList
        fields = '__all__'

class SingleServiceSerializer(serializers.ModelSerializer):
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
    payment_info = ServicePaymnetSerializer(read_only=True)
    why_choose_us_title = ServiceWhyChooseUsTitleSerializer(
        read_only=True, 
        source='service_why_choose_us_title'
    )
    why_choose_us_item = ServiceWhyChooseUsItemSerializer(
        many=True,
        read_only=True,
        source='service_why_choose_us_item'
    )
    compliance_title = ComplianceTitleSerializer(
        read_only=True, 
        source='service_compliance_title'
    )
    compliance_item = ComplianceItemListSerializer(
        many=True,
        read_only=True,
        source='service_compliance_item'
    )

    class Meta:
        model = Service
        fields = '__all__'

    def get_related_services(self, obj):
        qs = Service.objects.filter(categories__in=obj.categories.all()).exclude(id=obj.id).distinct()
        return RelatedServiceSerializer(qs, many=True, context=self.context).data
