from rest_framework import serializers
from .models import Address, AppUser, CustomerRelationship, OptimizedAppUser

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
    
class CustomerRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRelationship
        fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
    
    def get_customerrelationship(self, obj):
        try:
            rel = CustomerRelationship.objects.get(appuser=obj)
            return CustomerRelationshipSerializer(rel).data
        except CustomerRelationship.DoesNotExist:
            return None

class OptimizedAppUserSerializer(serializers.ModelSerializer):
    address_city = serializers.CharField(source='address.city')
    address_country = serializers.CharField(source='address.country')
    points = serializers.SerializerMethodField()

    class Meta:
        model = OptimizedAppUser
        fields = ['id','customer_id', 'first_name', 'last_name', 'gender', 'birthday', 'phone_number', 'address_city', 'address_country', 'points']

    def get_points(self, obj):
        rel_qs = getattr(obj, 'customerrelationship', None)
        if rel_qs:
            rel = rel_qs.first()
            if rel:
                return rel.points
        return None
